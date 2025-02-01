#!/bin/bash

echo "🚀 Installing Point Chamber Extractor..."

# ---- CHECK IF GIT IS INSTALLED ----
if ! command -v git &> /dev/null
then
    echo "❌ Git is not installed! Please install Git and try again."
    exit 1
fi

# ---- CHECK IF PYTHON IS INSTALLED ----
if ! command -v python3 &> /dev/null
then
    echo "⚠️  Python3 not found. Installing Python..."
    
    # macOS (using Homebrew)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "❌ Homebrew is not installed. Please install it first: https://brew.sh/"
            exit 1
        fi
        brew install python
    fi

    # Debian-based Linux (Ubuntu, etc.)
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && sudo apt install -y python3 python3-venv
    fi
fi

# ---- CLONE THE REPO ----
if [ ! -d "point-chamber-extractor" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/derek-dahl/point-chamber-extractor.git
fi

# Navigate into the project folder
cd point-chamber-extractor

# ---- CREATE A VIRTUAL ENVIRONMENT ----
echo "🐍 Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# ---- INSTALL DEPENDENCIES ----
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
else
    echo "⚠️  Warning: requirements.txt not found. Installing 'requests' manually..."
    pip install requests
fi

# ---- RUN THE PROGRAM ----
echo "🔄 Running extractor..."
python3 main.py

echo "🎉 Setup complete! Data has been extracted and saved."
