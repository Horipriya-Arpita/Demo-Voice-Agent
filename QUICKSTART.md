# Quick Start Guide

Get your voice agent running in 5 minutes!

## Step 1: Install Dependencies

**Windows:**
```bash
.\setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Step 2: Get Your API Keys (Free)

### Daily.co (WebRTC)
1. Go to [https://dashboard.daily.co/signup](https://dashboard.daily.co/signup)
2. Sign up for free account
3. Copy your API key from [Developers page](https://dashboard.daily.co/developers)
4. Create a room and copy the room URL

### Deepgram (Speech-to-Text)
1. Go to [https://console.deepgram.com/signup](https://console.deepgram.com/signup)
2. Sign up for free (45,000 minutes/month)
3. Copy your API key from [API Keys](https://console.deepgram.com/project/default/settings/api-keys)

### Groq (LLM - Recommended)
1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for free account
3. Copy your API key from [API Keys](https://console.groq.com/keys)

## Step 3: Configure

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env  # macOS/Linux
   copy .env.example .env  # Windows
   ```

2. Edit `.env` and add your API keys:
   ```env
   DAILY_API_KEY=your_daily_api_key
   DAILY_ROOM_URL=https://your-domain.daily.co/your-room
   DEEPGRAM_API_KEY=your_deepgram_api_key
   GROQ_API_KEY=your_groq_api_key
   TTS_PROVIDER=deepgram
   ```

## Step 4: Run!

```bash
python -m src.main
```

## Step 5: Connect

1. Open your `DAILY_ROOM_URL` in a browser
2. Allow microphone access
3. Start talking!

## That's It!

You now have a working voice agent. For more details, see [README.md](README.md).

## Troubleshooting

**"Missing required environment variables"**
- Check your `.env` file has all keys set
- Remove any spaces around `=` signs

**"No module named 'pipecat'"**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

**Can't hear the agent**
- Check your browser has speaker permissions
- Verify DAILY_ROOM_URL is correct
- Try refreshing the browser page

## Next Steps

- Customize `BOT_INSTRUCTIONS` in `.env`
- Try different LLM models
- Add conversation memory
- Deploy to the cloud

Enjoy your voice agent! 🎤
