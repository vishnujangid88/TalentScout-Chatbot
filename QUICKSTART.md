# 🚀 Quick Start Guide

Get up and running with the TalentScout Hiring Assistant in 5 minutes!

## Prerequisites

- Python 3.9 or higher
- An API key from [OpenAI](https://platform.openai.com/api-keys) or [Groq](https://console.groq.com/) (Groq is FREE!)

## Installation Steps

### 1. Clone the Project

```bash
git clone https://github.com/vishnujangid88/TalentScout-Chatbot.git
cd TalentScout-Chatbot
pip install -r requirements.txt
```

### 2. Set Up API Key

**Option A: Using .env file (Recommended for local development)**

1. Copy the example file:
   ```bash
   # Windows
   copy .env.example .env
   
   # macOS/Linux
   cp .env.example .env
   ```

2. Edit `.env` and add your API key:
   ```env
   # Prefer Groq (free tier)
   GROQ_API_KEY=your-groq-key-here
   LLM_PROVIDER=groq
   MODEL_NAME=llama-3.1-8b-instant

   # Optional OpenAI fallback
   OPENAI_API_KEY=sk-your-key-here
   # MODEL_NAME=gpt-3.5-turbo
   ```

**Option B: Using Streamlit Secrets (For deployment)**

1. Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your-groq-key-here"
   MODEL_NAME = "llama-3.1-8b-instant"
   LLM_PROVIDER = "groq"
   ```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

The app will automatically open at `http://localhost:8501`

## Verify Setup

Run the setup check script:

```bash
python setup_check.py
```

This will verify:
- ✅ Python version
- ✅ Installed dependencies
- ✅ API key configuration
- ✅ Project structure

## Getting API Keys

### OpenAI (Paid)

1. Visit [platform.openai.com](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Add $5-10 credit to your account
5. Use model: `gpt-3.5-turbo`

### Groq (FREE - Recommended for Testing)

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up with your email
3. Go to API Keys section
4. Create a new API key
5. Free tier: 14,400 requests/day
6. Use model: `llama3-70b-8192`
   - Recommended current option: `llama-3.1-8b-instant`

## Troubleshooting

### "API key not found" Error

- Make sure `.env` file exists in the project root
- Check that your API key is correctly set in `.env`
- For deployment, add secrets in Streamlit Cloud or Hugging Face Spaces

### "Module not found" Error

- Run: `pip install -r requirements.txt`
- Make sure you're in the correct virtual environment

### App won't start

- Check Python version: `python --version` (should be 3.9+)
- Verify all files are in place: `python setup_check.py`
- Check for error messages in the terminal

## Next Steps

1. ✅ Test the chatbot locally
2. 📖 Read the full [README.md](README.md) for detailed documentation
3. 🚀 Visit the live demo on Streamlit Cloud: https://talentscout-chat.streamlit.app/
4. 🎨 Customize prompts and styling to match your brand

## Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review the code comments for implementation details
- Open an issue on GitHub if you encounter bugs

---

**Happy coding! 🎉**


