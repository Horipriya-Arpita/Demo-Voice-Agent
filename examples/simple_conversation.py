"""
Simple example of running the voice agent.

This example demonstrates the basic usage of the voice agent.
Make sure you have:
1. Set up your .env file with required API keys
2. Created a Daily.co room
3. Installed dependencies: pip install -r requirements.txt
"""

import asyncio
from src.bot import run_voice_agent
from src.config import Config


async def main():
    """Run a simple voice conversation."""
    # Load configuration from environment
    config = Config.from_env()

    print(f"\n{'='*60}")
    print(f"  Voice Agent - Simple Conversation Example")
    print(f"{'='*60}")
    print(f"\nBot Name: {config.bot_name}")
    print(f"Room URL: {config.daily_room_url}")
    print(f"\nInstructions:")
    print(f"1. Open the Room URL in your browser")
    print(f"2. Allow microphone and speaker access")
    print(f"3. Start talking to the agent!")
    print(f"\nPress Ctrl+C to stop the agent\n")
    print(f"{'='*60}\n")

    # Run the voice agent
    await run_voice_agent(config)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nAgent stopped by user")
