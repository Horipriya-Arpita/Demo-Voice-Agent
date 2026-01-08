# Voice Agent with Pipecat

A real-time conversational AI voice agent built with [Pipecat](https://github.com/pipecat-ai/pipecat), featuring low-latency WebRTC audio streaming and natural voice interactions.

## Features

- **Real-time Voice Conversations**: Low-latency bidirectional audio streaming via WebRTC
- **Natural Language Processing**: Powered by state-of-the-art LLMs (OpenAI GPT-4o-mini or Groq Llama 3.1)
- **High-Quality Voice**: Natural text-to-speech with Deepgram or ElevenLabs
- **Accurate Speech Recognition**: Using Deepgram's advanced STT technology
- **Free Tier Friendly**: Configured to use free tiers of all services (~10,000 minutes/month)
- **Easy Configuration**: Simple environment variable setup
- **Extensible**: Built on Pipecat's modular pipeline architecture

## Architecture

```
Audio Input → STT (Deepgram) → LLM (OpenAI/Groq) → TTS (Deepgram/ElevenLabs) → Audio Output
                                        ↓
                              Daily.co WebRTC Transport
```

## Prerequisites

- Python 3.10 or higher
- A microphone and speakers/headphones
- API keys for the following services (all have free tiers):
  - [Daily.co](https://daily.co) - WebRTC infrastructure
  - [Deepgram](https://deepgram.com) - Speech-to-Text
  - [OpenAI](https://openai.com) OR [Groq](https://groq.com) - Large Language Model
  - [ElevenLabs](https://elevenlabs.io) (optional) - Text-to-Speech

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd Voice-Agent

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Get API Keys

#### Daily.co (Required)
1. Sign up at [https://dashboard.daily.co/signup](https://dashboard.daily.co/signup)
2. Go to the [Developers page](https://dashboard.daily.co/developers)
3. Copy your API key
4. Create a room:
   - Go to [Rooms](https://dashboard.daily.co/rooms)
   - Click "Create room"
   - Copy the room URL (e.g., `https://your-domain.daily.co/your-room`)

#### Deepgram (Required)
1. Sign up at [https://console.deepgram.com/signup](https://console.deepgram.com/signup)
2. Get 45,000 free minutes per month
3. Go to [API Keys](https://console.deepgram.com/project/default/settings/api-keys)
4. Create and copy your API key

#### LLM Provider (Choose One)

**Option A: Groq (Recommended - Free)**
1. Sign up at [https://console.groq.com](https://console.groq.com)
2. Get your API key from [API Keys page](https://console.groq.com/keys)
3. Free tier includes fast inference with Llama 3.1 70B

**Option B: OpenAI**
1. Sign up at [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. Get $5 in free trial credits
3. Get your API key from [API Keys page](https://platform.openai.com/api-keys)

#### TTS Provider (Optional)

**Using Deepgram TTS (Recommended - Bundled with STT)**
- No additional setup needed if you have Deepgram STT
- Set `TTS_PROVIDER=deepgram` in your .env file

**Using ElevenLabs (Higher Quality)**
1. Sign up at [https://elevenlabs.io](https://elevenlabs.io)
2. Get 10,000 characters per month free
3. Get your API key from [Profile Settings](https://elevenlabs.io/app/settings)
4. (Optional) Choose a voice and copy its Voice ID

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your favorite editor
# Add your API keys and Daily.co room URL
```

Example [.env](.env.example) file:
```env
# Daily.co Configuration
DAILY_API_KEY=your_daily_api_key_here
DAILY_ROOM_URL=https://your-domain.daily.co/your-room

# Deepgram Configuration
DEEPGRAM_API_KEY=your_deepgram_api_key_here

# LLM Configuration (Groq recommended for free tier)
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-70b-versatile

# TTS Configuration
TTS_PROVIDER=deepgram

# Bot Configuration
BOT_NAME=Voice Assistant
BOT_INSTRUCTIONS=You are a helpful AI voice assistant. Keep your responses concise and natural for voice conversation.

# Logging
LOG_LEVEL=INFO
```

### 4. Run the Voice Agent

```bash
# Run the main application
python -m src.main

# Or run the example
python examples/simple_conversation.py
```

### 5. Connect to Your Agent

1. Open the Daily.co room URL in your browser (the one you set in DAILY_ROOM_URL)
2. Allow microphone and speaker access when prompted
3. Start talking to your voice agent!

## Project Structure

```
Voice-Agent/
├── .env                          # Your API keys (not committed to git)
├── .env.example                  # Example environment file
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── src/
│   ├── __init__.py
│   ├── main.py                   # Application entry point
│   ├── bot.py                    # Voice agent implementation
│   ├── config.py                 # Configuration management
│   └── utils/
│       ├── __init__.py
│       └── logger.py             # Logging utilities
├── tests/
│   ├── __init__.py
│   └── test_bot.py               # Unit tests (coming soon)
└── examples/
    └── simple_conversation.py    # Example usage
```

## Configuration Options

### LLM Providers

**OpenAI (GPT-4o-mini)**
```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

**Groq (Llama 3.1)**
```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-70b-versatile
```

### TTS Providers

**Deepgram TTS**
```env
TTS_PROVIDER=deepgram
```

**ElevenLabs**
```env
TTS_PROVIDER=elevenlabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM  # Optional, Rachel voice
```

### Bot Customization

```env
BOT_NAME=My Custom Assistant
BOT_INSTRUCTIONS=You are a specialized assistant for customer support. Be professional and helpful.
LOG_LEVEL=DEBUG  # Options: DEBUG, INFO, WARNING, ERROR
```

## Free Tier Limits

With the recommended free tier configuration:

| Service | Free Tier | Monthly Usage |
|---------|-----------|---------------|
| Daily.co | 10,000 minutes | WebRTC streaming |
| Deepgram STT | 45,000 minutes | Speech recognition |
| Groq | Free (rate limited) | LLM inference |
| Deepgram TTS | Included with STT | Voice synthesis |
| **Total** | **~10,000 minutes** | **Voice conversations** |

## Troubleshooting

### "Missing required environment variables"
- Make sure you've created a `.env` file (copy from `.env.example`)
- Check that all required API keys are set
- Verify there are no extra spaces around the `=` sign

### "No LLM provider configured"
- Set either `OPENAI_API_KEY` or `GROQ_API_KEY` in your `.env` file
- The bot requires at least one LLM provider to function

### Audio issues
- Ensure your browser has microphone and speaker permissions
- Try using headphones to prevent echo
- Check the Daily.co room is properly configured
- Verify your DAILY_ROOM_URL is correct

### Connection fails
- Verify your `DAILY_API_KEY` is correct
- Check that your Daily.co room URL is valid and active
- Ensure your internet connection is stable

### High latency
- Consider using Groq instead of OpenAI (faster inference)
- Check your internet connection speed
- Reduce bot instruction complexity for faster responses

## Advanced Usage

### Customizing the Bot Personality

Edit the `BOT_INSTRUCTIONS` in your `.env` file:

```env
BOT_INSTRUCTIONS=You are a friendly cooking assistant. Help users with recipes and cooking tips. Keep responses brief and encouraging.
```

### Using Local LLM (Ollama)

For completely free, offline LLM:

1. Install [Ollama](https://ollama.ai)
2. Pull a model: `ollama pull llama3.1`
3. Modify [src/bot.py](src/bot.py) to use Ollama endpoint
4. No API key needed!

### Adding Conversation Memory

The current implementation is stateless. To add memory:

1. Store conversation history in a list or database
2. Pass context to the LLM in the pipeline
3. Implement a conversation manager

### Deploying to Production

For deployment beyond local testing:

**Free hosting options:**
- [Render](https://render.com) - Free tier available
- [Railway](https://railway.app) - Free trial credits
- [Fly.io](https://fly.io) - Free tier for small apps

**Steps:**
1. Set environment variables in your hosting platform
2. Ensure your Daily.co room is permanent (not temporary)
3. Monitor API usage to stay within free tiers
4. Consider implementing rate limiting

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Resources

- [Pipecat Documentation](https://docs.pipecat.ai)
- [Pipecat GitHub Examples](https://github.com/pipecat-ai/pipecat/tree/main/examples)
- [Daily.co Python SDK](https://docs.daily.co/reference/daily-python)
- [Deepgram API Docs](https://developers.deepgram.com)
- [Groq API Docs](https://console.groq.com/docs)
- [OpenAI API Docs](https://platform.openai.com/docs)

## License

This project is open source and available under the MIT License.

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review your `.env` configuration
3. Check the console logs for error messages
4. Ensure all API keys are valid and services are active

## Acknowledgments

Built with:
- [Pipecat](https://github.com/pipecat-ai/pipecat) - Voice agent framework
- [Daily.co](https://daily.co) - WebRTC infrastructure
- [Deepgram](https://deepgram.com) - Speech recognition and synthesis
- [Groq](https://groq.com) - Fast LLM inference
- [OpenAI](https://openai.com) - GPT models

---

**Happy voice chatting!** 🎤🤖
