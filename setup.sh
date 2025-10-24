#!/bin/bash

# Telegram Session Monitor Bot - Quick Setup Launcher

echo "🤖 Telegram Session Monitor Bot - Quick Setup"
echo "============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
    
    echo "📥 Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "🔧 Activating existing virtual environment..."
    source venv/bin/activate
fi

# Check if already configured
if [ -f "config.json" ]; then
    # Check if it's a real config (not template)
    if grep -q "YOUR_API_ID" config.json 2>/dev/null; then
        echo "⚙️  Configuration template found, starting setup..."
        python setup_api.py
    else
        echo "✅ Bot already configured!"
        echo ""
        echo "Choose an option:"
        echo "1. Start the bot"
        echo "2. Reconfigure API credentials"
        echo "3. Exit"
        echo ""
        read -p "Enter choice (1-3): " choice
        
        case $choice in
            1)
                echo "🚀 Starting bot..."
                python main.py
                ;;
            2)
                echo "🔄 Reconfiguring..."
                python setup_api.py
                ;;
            3)
                echo "👋 Goodbye!"
                exit 0
                ;;
            *)
                echo "❌ Invalid choice!"
                exit 1
                ;;
        esac
    fi
else
    echo "⚙️  No configuration found, starting initial setup..."
    python setup_api.py
fi

echo ""
echo "🎉 Setup complete! You can now run 'python main.py' to start your bot."
