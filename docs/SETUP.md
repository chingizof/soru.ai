# Detailed Setup Guide

This guide provides detailed instructions for setting up Soru.ai on your local machine.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Getting API Keys](#getting-api-keys)
3. [Installation Steps](#installation-steps)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **Python**: 3.11 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 2GB free space
- **Internet**: Active internet connection for API calls

### Supported Operating Systems
- macOS 10.15+
- Ubuntu 20.04+
- Windows 10/11
- Other Unix-like systems

---

## Getting API Keys

### Google Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Click "Get API Key" button
4. Create a new project or select existing one
5. Copy your API key
6. Keep it secure - never commit to version control

**Free Tier Limits:**
- 60 requests per minute
- Perfect for development and personal use

### Hugging Face API Token

1. Visit [Hugging Face](https://huggingface.co/)
2. Create an account or sign in
3. Go to Settings → Access Tokens
4. Click "New token"
5. Give it a name (e.g., "Soru.ai")
6. Select "Read" access
7. Copy your token

**Free Tier:**
- Unlimited requests
- May experience rate limiting during high traffic

---

## Installation Steps

### 1. Clone the Repository

```bash
# HTTPS
git clone https://github.com/yourusername/soru.ai.git

# SSH
git clone git@github.com:yourusername/soru.ai.git

# Navigate to directory
cd soru.ai
```

### 2. Set Up Virtual Environment

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (should show venv path)
which python
```

#### Windows
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify activation
where python
```

### 3. Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

**Expected packages:**
- reflex
- google-generativeai
- transformers
- requests
- python-dotenv
- youtube-transcript-api
- And their dependencies

---

## Configuration

### 1. Create Environment File

```bash
# Copy example file
cp .env.example .env

# Edit with your favorite editor
nano .env
# or
vim .env
# or
code .env  # VSCode
```

### 2. Add Your API Keys

Edit `.env` file:

```env
# Google Gemini API Configuration
GOOGLE_API_KEY=AIzaSyC...your_actual_key_here...XYZ

# Hugging Face API Configuration
HUGGINGFACE_API_KEY=hf_...your_actual_token_here...
HUGGINGFACE_API_URL=https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten

# Application Configuration
APP_NAME=lahacks_24
DEBUG=False
```

**Important:**
- Replace placeholder values with your actual keys
- Never share or commit this file
- Keep backups in a secure location

### 3. Initialize Reflex

```bash
# Initialize Reflex application
reflex init

# This creates necessary configuration files
```

---

## Running the Application

### Development Mode

```bash
# Start development server
reflex run

# With hot reload (auto-restart on changes)
reflex run --env dev
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000

### Production Mode

```bash
# Build for production
reflex export

# Run production build
reflex run --env prod
```

---

## Troubleshooting

### Common Issues

#### Issue: "Module not found" errors

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: "API key not found" error

**Solution:**
1. Check `.env` file exists
2. Verify API keys are correct
3. Ensure no extra spaces around keys
4. Try printing config: `python -c "from lahacks_24.config import Config; print(Config.GOOGLE_API_KEY[:10])"`

#### Issue: Reflex won't start

**Solution:**
```bash
# Clean Reflex cache
rm -rf .web

# Reinitialize
reflex init
reflex run
```

#### Issue: Port already in use

**Solution:**
```bash
# Find process using port 3000
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill the process or use different port
reflex run --port 3001
```

#### Issue: OCR not working

**Solution:**
1. Verify Hugging Face API key is correct
2. Check internet connection
3. Try a different image (clear handwriting)
4. Check API status: https://status.huggingface.co/

#### Issue: YouTube transcript not found

**Solution:**
1. Ensure video has captions enabled
2. Try a different video
3. Check if video is public
4. Some videos don't have transcripts available

### Performance Issues

#### Slow flashcard generation

**Causes & Solutions:**
1. **First request**: Models need to load (30-60 seconds)
2. **Large images**: Resize images to < 2MB
3. **Long videos**: Use shorter videos (< 30 minutes)
4. **API rate limits**: Wait a minute and try again

#### High memory usage

**Solutions:**
1. Restart the application periodically
2. Clear `uploaded_files/` directory
3. Close other applications
4. Upgrade to 8GB+ RAM if possible

---

## Testing Your Setup

### 1. Test Environment

```bash
python -c "from lahacks_24.config import Config; Config.validate()"
```

Expected output:
```
✅ All configuration values are set
```

### 2. Test OCR

Create a test script `test_ocr.py`:

```python
import asyncio
from lahacks_24.utils.ocr import extract_text_from_image

async def test():
    with open("test_image.jpg", "rb") as f:
        text = await extract_text_from_image(f.read())
        print(f"Extracted: {text}")

asyncio.run(test())
```

### 3. Test AI Generation

Create a test script `test_ai.py`:

```python
import asyncio
from lahacks_24.utils.ai import create_flashcard_prompt, generate_flashcards

async def test():
    prompt = create_flashcard_prompt("Python is a programming language")
    cards = await generate_flashcards(prompt)
    print(cards)

asyncio.run(test())
```

---

## Next Steps

After successful setup:

1. Read the [API Documentation](API.md)
2. Check out [Contributing Guide](../CONTRIBUTING.md)
3. Join our [Discord community](https://discord.gg/soruai)
4. Star the repository on GitHub ⭐

---

## Getting Help

If you're still experiencing issues:

1. Check [GitHub Issues](https://github.com/yourusername/soru.ai/issues)
2. Ask in [Discussions](https://github.com/yourusername/soru.ai/discussions)
3. Join our [Discord](https://discord.gg/soruai)
4. Email: support@soru.ai

**When asking for help, include:**
- Operating system and version
- Python version (`python --version`)
- Error messages (full traceback)
- Steps to reproduce the issue

