"""Main entry point for the voice agent."""

import asyncio
import sys
from pathlib import Path

from src.bot import run_voice_agent
from src.config import Config
from src.utils.logger import setup_logger


def main():
    """Main function to run the voice agent."""
    logger = setup_logger("main")

    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = Config.from_env()
        config.validate()

        # Log configuration (without sensitive data)
        logger.info(f"Bot Name: {config.bot_name}")
        logger.info(f"LLM Provider: {config.get_llm_provider()}")
        logger.info(f"TTS Provider: {config.tts_provider}")
        logger.info(f"Log Level: {config.log_level}")

        # Run the voice agent
        logger.info("Starting voice agent...")
        asyncio.run(run_voice_agent(config))

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        logger.info("\nPlease ensure you have:")
        logger.info("1. Created a .env file (copy from .env.example)")
        logger.info("2. Set all required API keys in your .env file")
        logger.info("3. Created a Daily.co room and set the DAILY_ROOM_URL")
        sys.exit(1)

    except KeyboardInterrupt:
        logger.info("\nShutdown requested by user")
        sys.exit(0)

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
