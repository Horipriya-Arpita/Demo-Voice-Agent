"""Configuration management for the voice agent."""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration class for the voice agent."""

    # Daily.co Configuration
    daily_api_key: str
    daily_room_url: str

    # Deepgram Configuration
    deepgram_api_key: str

    # LLM Configuration
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"
    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.1-70b-versatile"

    # TTS Configuration
    tts_provider: str = "deepgram"  # Options: deepgram, elevenlabs
    elevenlabs_api_key: Optional[str] = None
    elevenlabs_voice_id: Optional[str] = None

    # Bot Configuration
    bot_name: str = "Voice Assistant"
    bot_instructions: str = "You are a helpful AI voice assistant. Keep your responses concise and natural for voice conversation."

    # Logging
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Config":
        """
        Load configuration from environment variables.

        Returns:
            Config instance with values from environment

        Raises:
            ValueError: If required environment variables are missing
        """
        # Load .env file if it exists
        load_dotenv()

        # Required fields
        daily_api_key = os.getenv("DAILY_API_KEY")
        daily_room_url = os.getenv("DAILY_ROOM_URL")
        deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

        # Validate required fields
        missing_fields = []
        if not daily_api_key:
            missing_fields.append("DAILY_API_KEY")
        if not daily_room_url:
            missing_fields.append("DAILY_ROOM_URL")
        if not deepgram_api_key:
            missing_fields.append("DEEPGRAM_API_KEY")

        if missing_fields:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_fields)}\n"
                f"Please set them in your .env file or environment."
            )

        # Optional LLM configuration
        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        groq_api_key = os.getenv("GROQ_API_KEY")
        groq_model = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")

        # Validate that at least one LLM is configured
        if not openai_api_key and not groq_api_key:
            raise ValueError(
                "At least one LLM provider must be configured.\n"
                "Please set either OPENAI_API_KEY or GROQ_API_KEY in your .env file."
            )

        # TTS configuration
        tts_provider = os.getenv("TTS_PROVIDER", "deepgram")
        elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        elevenlabs_voice_id = os.getenv("ELEVENLABS_VOICE_ID")

        # Validate TTS configuration
        if tts_provider == "elevenlabs" and not elevenlabs_api_key:
            raise ValueError(
                "ELEVENLABS_API_KEY is required when TTS_PROVIDER is set to 'elevenlabs'"
            )

        # Bot configuration
        bot_name = os.getenv("BOT_NAME", "Voice Assistant")
        bot_instructions = os.getenv(
            "BOT_INSTRUCTIONS",
            "You are a helpful AI voice assistant. Keep your responses concise and natural for voice conversation."
        )

        # Logging
        log_level = os.getenv("LOG_LEVEL", "INFO")

        return cls(
            daily_api_key=daily_api_key,
            daily_room_url=daily_room_url,
            deepgram_api_key=deepgram_api_key,
            openai_api_key=openai_api_key,
            openai_model=openai_model,
            groq_api_key=groq_api_key,
            groq_model=groq_model,
            tts_provider=tts_provider,
            elevenlabs_api_key=elevenlabs_api_key,
            elevenlabs_voice_id=elevenlabs_voice_id,
            bot_name=bot_name,
            bot_instructions=bot_instructions,
            log_level=log_level,
        )

    def get_llm_provider(self) -> str:
        """
        Determine which LLM provider to use.

        Returns:
            "openai" or "groq" based on available API keys
        """
        if self.openai_api_key:
            return "openai"
        elif self.groq_api_key:
            return "groq"
        else:
            raise ValueError("No LLM provider configured")

    def validate(self) -> None:
        """
        Validate the configuration.

        Raises:
            ValueError: If configuration is invalid
        """
        # Already validated in from_env, but can add additional checks here
        if self.tts_provider not in ["deepgram", "elevenlabs"]:
            raise ValueError(
                f"Invalid TTS provider: {self.tts_provider}. "
                f"Must be 'deepgram' or 'elevenlabs'"
            )
