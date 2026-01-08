"""Voice agent bot implementation using Pipecat."""

import asyncio
from typing import Optional

from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineTask
from pipecat.processors.aggregators.llm_response import (
    LLMAssistantContextAggregator,
    LLMUserContextAggregator,
)
from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.services.deepgram.tts import DeepgramTTSService
from pipecat.services.openai.llm import OpenAILLMService
from pipecat.transports.daily.transport import DailyParams, DailyTransport
from pipecat.audio.vad.silero import SileroVADAnalyzer

from src.config import Config
from src.utils.logger import setup_logger


class VoiceAgent:
    """Voice agent that handles real-time conversations using Pipecat."""

    def __init__(self, config: Config):
        """
        Initialize the voice agent.

        Args:
            config: Configuration object with API keys and settings
        """
        self.config = config
        self.logger = setup_logger("VoiceAgent", config.log_level)
        self.transport: Optional[DailyTransport] = None
        self.runner: Optional[PipelineRunner] = None

    async def run(self):
        """
        Run the voice agent.

        This sets up the Pipecat pipeline and starts processing audio.
        """
        try:
            self.logger.info("Initializing voice agent...")

            # Initialize Daily transport for WebRTC
            transport = DailyTransport(
                self.config.daily_room_url,
                None,  # No token needed for development
                self.config.bot_name,
                DailyParams(
                    api_key=self.config.daily_api_key,
                    audio_in_enabled=True,
                    audio_out_enabled=True,
                    transcription_enabled=True,
                    vad_analyzer=SileroVADAnalyzer(),
                ),
            )
            self.transport = transport

            # Initialize Speech-to-Text (Deepgram)
            stt = DeepgramSTTService(api_key=self.config.deepgram_api_key)

            # Initialize LLM
            llm = self._initialize_llm()

            # Initialize Text-to-Speech
            tts = self._initialize_tts()

            # Create message aggregators
            user_response = LLMUserContextAggregator()
            assistant_response = LLMAssistantContextAggregator()

            # Build the pipeline
            # Audio Input -> STT -> User Aggregator -> LLM -> Assistant Aggregator -> TTS -> Audio Output
            pipeline = Pipeline(
                [
                    transport.input(),  # Audio input from Daily
                    stt,  # Speech to text
                    user_response,  # Aggregate user messages
                    llm,  # Language model processing
                    tts,  # Text to speech
                    transport.output(),  # Audio output to Daily
                    assistant_response,  # Aggregate assistant messages
                ]
            )

            # Create pipeline task
            task = PipelineTask(pipeline)

            # Create and configure runner
            self.runner = PipelineRunner()

            # Log connection info
            self.logger.info(f"Voice agent ready!")
            self.logger.info(f"Room URL: {self.config.daily_room_url}")
            self.logger.info(f"Join the room to start talking to the agent")

            # Run the pipeline
            await self.runner.run(task)

        except Exception as e:
            self.logger.error(f"Error running voice agent: {e}", exc_info=True)
            raise

    def _initialize_llm(self):
        """
        Initialize the LLM service based on configuration.

        Returns:
            Configured LLM service

        Raises:
            ValueError: If LLM provider is not supported
        """
        llm_provider = self.config.get_llm_provider()

        if llm_provider == "openai":
            self.logger.info(f"Using OpenAI LLM: {self.config.openai_model}")
            return OpenAILLMService(
                api_key=self.config.openai_api_key,
                model=self.config.openai_model,
            )

        elif llm_provider == "groq":
            self.logger.info(f"Using Groq LLM: {self.config.groq_model}")
            # Groq uses OpenAI-compatible API
            return OpenAILLMService(
                api_key=self.config.groq_api_key,
                base_url="https://api.groq.com/openai/v1",
                model=self.config.groq_model,
            )

        else:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")

    def _initialize_tts(self):
        """
        Initialize the TTS service based on configuration.

        Returns:
            Configured TTS service

        Raises:
            ValueError: If TTS provider is not supported
        """
        if self.config.tts_provider == "deepgram":
            self.logger.info("Using Deepgram TTS")
            return DeepgramTTSService(
                api_key=self.config.deepgram_api_key,
                voice="aura-asteria-en",  # Natural female voice
            )

        elif self.config.tts_provider == "elevenlabs":
            self.logger.info("Using ElevenLabs TTS")
            from pipecat.services.elevenlabs import ElevenLabsTTSService

            return ElevenLabsTTSService(
                api_key=self.config.elevenlabs_api_key,
                voice_id=self.config.elevenlabs_voice_id or "21m00Tcm4TlvDq8ikWAM",  # Default voice
            )

        else:
            raise ValueError(f"Unsupported TTS provider: {self.config.tts_provider}")

    async def cleanup(self):
        """Clean up resources."""
        self.logger.info("Cleaning up voice agent...")
        if self.runner:
            try:
                await self.runner.stop()
            except Exception as e:
                self.logger.error(f"Error stopping runner: {e}")


async def run_voice_agent(config: Config):
    """
    Run the voice agent with proper error handling and cleanup.

    Args:
        config: Configuration object
    """
    agent = VoiceAgent(config)
    try:
        await agent.run()
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await agent.cleanup()
