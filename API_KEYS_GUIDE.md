# API Keys Setup Guide

This guide helps you get all the free API keys needed for your voice agent.

## Summary of Free Tiers

| Service | Free Tier | What It Does | Sign Up Link |
|---------|-----------|--------------|--------------|
| **Daily.co** | 10,000 min/month | WebRTC streaming | [Sign up](https://dashboard.daily.co/signup) |
| **Deepgram** | 45,000 min/month | Speech-to-Text + TTS | [Sign up](https://console.deepgram.com/signup) |
| **Groq** | Free (rate limited) | Fast LLM inference | [Sign up](https://console.groq.com) |
| **Total** | **~10,000 minutes** | **Voice conversations** | - |

---

## 1. Daily.co (Required)

**What it does:** Handles WebRTC audio streaming between you and the bot

**Free tier:** 10,000 minutes per month

### Setup Steps:

1. **Sign up:** [https://dashboard.daily.co/signup](https://dashboard.daily.co/signup)

2. **Get API Key:**
   - Go to [Developers page](https://dashboard.daily.co/developers)
   - Copy your API key
   - Add to `.env`: `DAILY_API_KEY=your_key_here`

3. **Create a Room:**
   - Go to [Rooms](https://dashboard.daily.co/rooms)
   - Click "Create room"
   - Choose any name (e.g., "voice-agent-room")
   - Copy the room URL (e.g., `https://yourname.daily.co/voice-agent-room`)
   - Add to `.env`: `DAILY_ROOM_URL=your_room_url`

**Time:** ~2 minutes

---

## 2. Deepgram (Required)

**What it does:** Converts speech to text (STT) and text to speech (TTS)

**Free tier:** 45,000 minutes per month (very generous!)

### Setup Steps:

1. **Sign up:** [https://console.deepgram.com/signup](https://console.deepgram.com/signup)

2. **Get API Key:**
   - After signup, you'll see the dashboard
   - Go to [API Keys](https://console.deepgram.com/project/default/settings/api-keys)
   - Click "Create New API Key"
   - Copy the key (you won't see it again!)
   - Add to `.env`: `DEEPGRAM_API_KEY=your_key_here`

3. **Set TTS Provider:**
   - Add to `.env`: `TTS_PROVIDER=deepgram`
   - This uses Deepgram for both STT and TTS (no extra cost)

**Time:** ~2 minutes

---

## 3. LLM Provider (Choose ONE)

### Option A: Groq (Recommended - Fastest & Free)

**What it does:** Provides the AI brain for conversation using Llama 3.1

**Free tier:** Free with rate limits (perfect for development)

**Setup Steps:**

1. **Sign up:** [https://console.groq.com](https://console.groq.com)

2. **Get API Key:**
   - Click on your profile (top right)
   - Go to [API Keys](https://console.groq.com/keys)
   - Click "Create API Key"
   - Copy the key
   - Add to `.env`:
     ```env
     GROQ_API_KEY=your_key_here
     GROQ_MODEL=llama-3.1-70b-versatile
     ```

**Why Groq?**
- ✅ Completely free
- ✅ Very fast inference (low latency)
- ✅ Great for real-time conversation
- ✅ No credit card required

**Time:** ~2 minutes

---

### Option B: OpenAI (Alternative)

**What it does:** Provides GPT-4o-mini for conversations

**Free tier:** $5 in trial credits (goes a long way with mini model)

**Setup Steps:**

1. **Sign up:** [https://platform.openai.com/signup](https://platform.openai.com/signup)

2. **Get API Key:**
   - Go to [API Keys](https://platform.openai.com/api-keys)
   - Click "Create new secret key"
   - Copy the key
   - Add to `.env`:
     ```env
     OPENAI_API_KEY=your_key_here
     OPENAI_MODEL=gpt-4o-mini
     ```

**Why OpenAI?**
- ✅ High-quality responses
- ✅ Well-documented
- ✅ Reliable
- ⚠️ Trial credits run out eventually

**Time:** ~3 minutes

---

## 4. ElevenLabs TTS (Optional - Better Voice Quality)

**What it does:** Provides more natural-sounding voices than Deepgram

**Free tier:** 10,000 characters per month

**Setup Steps:**

1. **Sign up:** [https://elevenlabs.io](https://elevenlabs.io)

2. **Get API Key:**
   - Go to [Profile Settings](https://elevenlabs.io/app/settings)
   - Copy your API key
   - Add to `.env`: `ELEVENLABS_API_KEY=your_key_here`

3. **Choose a Voice (Optional):**
   - Go to [Voice Library](https://elevenlabs.io/app/voice-library)
   - Browse and select a voice
   - Copy the Voice ID
   - Add to `.env`: `ELEVENLABS_VOICE_ID=your_voice_id`
   - Set provider: `TTS_PROVIDER=elevenlabs`

**Time:** ~3 minutes

**Note:** ElevenLabs free tier is limited (10k chars), so Deepgram TTS is recommended for longer conversations.

---

## Complete .env Example

Here's what your `.env` should look like with all keys:

```env
# Daily.co Configuration (Required)
DAILY_API_KEY=sk_live_xxxxxxxxxxxxxxxx
DAILY_ROOM_URL=https://yourname.daily.co/voice-agent-room

# Deepgram Configuration (Required)
DEEPGRAM_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# LLM Configuration - Groq (Recommended)
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GROQ_MODEL=llama-3.1-70b-versatile

# OR use OpenAI instead
# OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# OPENAI_MODEL=gpt-4o-mini

# TTS Configuration
TTS_PROVIDER=deepgram

# Optional: Use ElevenLabs for better voice quality
# TTS_PROVIDER=elevenlabs
# ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM

# Bot Configuration
BOT_NAME=Voice Assistant
BOT_INSTRUCTIONS=You are a helpful AI voice assistant. Keep your responses concise and natural for voice conversation.

# Logging
LOG_LEVEL=INFO
```

---

## Security Tips

1. **Never commit `.env` to git** - It's already in `.gitignore`
2. **Don't share your API keys** - They give access to your accounts
3. **Rotate keys if exposed** - All services let you regenerate keys
4. **Use `.env.example` for sharing** - It shows structure without secrets

---

## Troubleshooting API Keys

### "Invalid API key" errors

1. **Check for extra spaces:**
   ```env
   # Wrong:
   DAILY_API_KEY = your_key_here

   # Correct:
   DAILY_API_KEY=your_key_here
   ```

2. **Verify key is complete:**
   - API keys are usually long (30+ characters)
   - Make sure you copied the entire key

3. **Check key is active:**
   - Log into the service dashboard
   - Verify the key hasn't been deleted

### "No LLM provider configured"

- Make sure you have EITHER `OPENAI_API_KEY` OR `GROQ_API_KEY` set
- You don't need both, just one

### "Room not found"

- Verify your `DAILY_ROOM_URL` is correct
- Check the room still exists in Daily.co dashboard
- Try creating a new room

---

## Cost Monitoring

### Staying Within Free Tiers

**Daily.co:**
- Monitor: [Dashboard](https://dashboard.daily.co)
- 10,000 minutes = ~167 hours of conversation
- Resets monthly

**Deepgram:**
- Monitor: [Usage Dashboard](https://console.deepgram.com/billing/usage)
- 45,000 minutes = ~750 hours
- Resets monthly

**Groq:**
- Monitor: [API Dashboard](https://console.groq.com)
- Free tier has rate limits (requests per minute)
- No hard usage cap

### If You Exceed Free Tier

1. **Daily.co:** Upgrade to pay-as-you-go ($0.0015/min)
2. **Deepgram:** Pay-as-you-go ($0.0043/min for STT)
3. **Groq:** Contact for pricing or use OpenAI
4. **Alternative:** Use local models (Ollama + Whisper)

---

## Next Steps

Once you have all your API keys:

1. ✅ Add them to your `.env` file
2. ✅ Run the agent: `python -m src.main`
3. ✅ Open your Daily.co room URL
4. ✅ Start talking!

Need help? Check [QUICKSTART.md](QUICKSTART.md) or [README.md](README.md)

---

**Total setup time: ~10 minutes** ⏱️

Happy chatting! 🎤🤖
