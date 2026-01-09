"""Local entry point for the voice agent (no Daily.co required)."""

import asyncio

from src.bot_local import run_local_voice_agent
from src.config import Config
from src.utils.logger import setup_logger


async def main():
    """Main entry point for the local voice agent."""
    logger = setup_logger("main", "INFO")

    try:
        logger.info("Loading configuration...")
        config = Config.from_env()

        # Log configuration (without sensitive keys)
        logger.info(f"Bot Name: {config.bot_name}")
        logger.info(f"LLM Provider: {config.get_llm_provider()}")
        logger.info(f"TTS Provider: {config.tts_provider}")
        logger.info(f"Log Level: {config.log_level}")

        logger.info("\n" + "="*50)
        logger.info("STARTING LOCAL VOICE AGENT")
        logger.info("="*50)
        logger.info("This will use your microphone and speakers directly.")
        logger.info("No WebRTC/Daily.co required!")
        logger.info("Press Ctrl+C to stop.")
        logger.info("="*50 + "\n")

        await run_local_voice_agent(config)

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        logger.info("\nPlease ensure you have:")
        logger.info("1. Created a .env file (copy from .env.example)")
        logger.info("2. Set DEEPGRAM_API_KEY")
        logger.info("3. Set either OPENAI_API_KEY or GROQ_API_KEY")
        logger.info("\nNote: DAILY_API_KEY and DAILY_ROOM_URL are NOT needed for local mode")
        return

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
