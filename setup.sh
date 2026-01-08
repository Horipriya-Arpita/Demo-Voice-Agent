#!/bin/bash
# Setup script for Voice Agent on macOS/Linux

echo "================================================"
echo "Voice Agent - Setup Script"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10 or higher"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo "[3/4] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[4/4] Setting up environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file from .env.example"
    echo ""
    echo "IMPORTANT: Edit .env file and add your API keys!"
else
    echo ".env file already exists, skipping..."
fi

echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys"
echo "2. Get API keys from:"
echo "   - Daily.co: https://dashboard.daily.co"
echo "   - Deepgram: https://console.deepgram.com"
echo "   - Groq: https://console.groq.com"
echo "3. Activate venv: source venv/bin/activate"
echo "4. Run the agent: python -m src.main"
echo ""
echo "================================================"
