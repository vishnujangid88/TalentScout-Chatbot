# 💼 TalentScout Hiring Assistant Chatbot

A sophisticated AI-powered hiring assistant chatbot built with Streamlit and Large Language Models (LLMs) to streamline the candidate screening process for TalentScout recruitment agency.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Prompt Engineering Approach](#prompt-engineering-approach)
- [Deployment](#deployment)
- [Challenges & Solutions](#challenges--solutions)
- [Future Improvements](#future-improvements)
- [Live Demo](#live-demo)
- [License](#license)

## 🎯 Project Overview

The TalentScout Hiring Assistant is an intelligent chatbot designed to automate the initial screening phase of the recruitment process. It collects candidate information systematically, validates inputs in real-time, and generates relevant technical questions based on the candidate's tech stack.

### What It Does

1. **Greets candidates** and explains the screening process
2. **Collects information** in a structured sequence:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position(s)
   - Current Location
   - Tech Stack
3. **Generates technical questions** (3-5 questions) based on the candidate's technologies
4. **Maintains conversation context** throughout the interaction
5. **Handles edge cases** gracefully (invalid inputs, exit requests, off-topic messages)

## ✨ Key Features

- ✅ **Sequential Information Collection**: Asks for one piece of information at a time
- ✅ **Real-time Input Validation**: Validates all inputs with helpful error messages
- ✅ **Dynamic Technical Questions**: Generates relevant questions based on tech stack
- ✅ **Context-Aware Conversations**: Maintains conversation history and context
- ✅ **Exit Handling**: Gracefully handles exit keywords (exit, quit, bye, etc.)
- ✅ **Fallback Responses**: Redirects off-topic conversations back to screening
- ✅ **Progress Tracking**: Visual progress indicator in sidebar
- ✅ **Modern UI**: Clean, professional interface with custom styling
- ✅ **Multi-LLM Support**: Supports both OpenAI and Groq APIs
- ✅ **Deployment Ready**: Configured for Streamlit Cloud and Hugging Face Spaces

## 🛠 Tech Stack

### Core Technologies
- **Python 3.9+**: Programming language
- **Streamlit 1.28+**: Web framework for UI
- **OpenAI API**: LLM provider (gpt-3.5-turbo)
- **Groq API**: Free alternative LLM provider (llama3-70b-8192)
- **LangChain**: Optional framework for LLM orchestration

### Key Libraries
- `streamlit`: UI framework
- `openai`: OpenAI API client
- `groq`: Groq API client (free alternative)
- `email-validator`: Email validation
- `phonenumbers`: Phone number validation and formatting
- `python-dotenv`: Environment variable management

## 📦 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- API key from OpenAI or Groq

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hiring-assistant-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy `.env.example` to `.env`:
   ```bash
   # On Windows
   copy .env.example .env
   
   # On macOS/Linux
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   MODEL_NAME=gpt-3.5-turbo
   LLM_PROVIDER=openai
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   
   Open your browser and navigate to `http://localhost:8501`

## ⚙️ Configuration

### API Key Setup

#### Option 1: OpenAI (Paid but Reliable)

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Add $5-10 credit to your account
5. Use model: `gpt-3.5-turbo` (most cost-effective)

#### Option 2: Groq (FREE - Recommended for Testing)

1. Go to [Groq Console](https://console.groq.com/)
2. Sign up with your email
3. Navigate to API Keys section
4. Create a new API key
5. Free tier: 14,400 requests per day
6. Use model: `llama3-70b-8192` or `mixtral-8x7b-32768`

### Environment Variables

Create a `.env` file in the root directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-key-here
MODEL_NAME=gpt-3.5-turbo

# Groq Configuration (Alternative)
GROQ_API_KEY=your-groq-key-here
# MODEL_NAME=llama3-70b-8192

# LLM Provider: "openai" or "groq"
LLM_PROVIDER=openai

# App Configuration
APP_TITLE=TalentScout Hiring Assistant
COMPANY_NAME=TalentScout
MAX_QUESTIONS=5
MIN_QUESTIONS=3
```

### Streamlit Secrets (For Deployment)

For Streamlit Cloud deployment, create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-your-key-here"
MODEL_NAME = "gpt-3.5-turbo"
LLM_PROVIDER = "openai"
APP_TITLE = "TalentScout Hiring Assistant"
COMPANY_NAME = "TalentScout"
MAX_QUESTIONS = 5
MIN_QUESTIONS = 3
```

## 📖 Usage Guide

### Starting a Conversation

1. Launch the application
2. The chatbot will automatically greet you
3. Follow the prompts to provide information

### Conversation Flow

1. **Greeting**: Bot introduces itself and asks for your name
2. **Name Collection**: Provide your full name
3. **Email Collection**: Provide your email address
4. **Phone Collection**: Provide your phone number (international format)
5. **Experience Collection**: Provide years of experience
6. **Position Collection**: Specify desired position(s)
7. **Location Collection**: Provide current location
8. **Tech Stack Collection**: List your technologies (comma-separated)
9. **Technical Questions**: Answer 3-5 technical questions
10. **Conclusion**: Receive summary and next steps

### Example Conversation

```
Bot: Hello! I'm the TalentScout Hiring Assistant. I'm here to help you through 
     our initial screening process. This will take just a few minutes. 
     May I have your full name to begin?

You: John Doe

Bot: Thank you, John! Could you please provide your email address?

You: john.doe@example.com

Bot: Great! Now, could you please provide your phone number in international 
     format (e.g., +1 234 567 8900)?

...
```

### Exit the Conversation

You can exit at any time by typing:
- `exit`
- `quit`
- `bye`
- `goodbye`
- `stop`
- `end`
- `cancel`

### Reset Conversation

Click the "🔄 Reset Conversation" button in the sidebar to start over.

## 📁 Project Structure

```
hiring-assistant-chatbot/
│
├── .streamlit/
│   ├── config.toml          # Streamlit theme configuration
│   └── secrets.toml.example  # API keys template (gitignored)
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore file
├── README.md                # This file
├── packages.txt             # System dependencies (for Hugging Face)
│
├── config/
│   ├── __init__.py
│   └── settings.py          # App settings, constants, stage definitions
│
├── prompts/
│   ├── __init__.py
│   ├── system_prompts.py    # All system prompts for different stages
│   └── question_bank.py     # Tech-specific question templates
│
├── utils/
│   ├── __init__.py
│   ├── llm_handler.py       # LLM API integration (OpenAI/Groq)
│   ├── conversation_manager.py  # State management, stage tracking
│   ├── validators.py        # Input validation functions
│   └── ui_components.py     # Reusable Streamlit UI components
│
└── assets/
    └── styles.css           # Custom CSS styling
```

### File Descriptions

- **app.py**: Main application entry point, handles UI and conversation flow
- **config/settings.py**: Configuration constants, stage definitions, API key management
- **prompts/system_prompts.py**: System prompts for each conversation stage
- **prompts/question_bank.py**: Pre-defined technical questions by technology
- **utils/llm_handler.py**: Handles LLM API calls (OpenAI/Groq)
- **utils/conversation_manager.py**: Manages conversation state and stages
- **utils/validators.py**: Input validation for all candidate information
- **utils/ui_components.py**: Reusable UI components for Streamlit

## 🧠 Prompt Engineering Approach

### Design Principles

1. **One Task at a Time**: Never ask for multiple pieces of information simultaneously
2. **Context Awareness**: Always pass collected information to maintain context
3. **Focused Responses**: System prompts emphasize staying on-topic
4. **Validation First**: Validate user input before sending to LLM
5. **Clear Instructions**: Explicit format requirements in prompts
6. **Fallback Handling**: Specific prompts for unclear/off-topic inputs

### System Prompt Structure

Each system prompt follows this pattern:

```
You are a [ROLE] for [COMPANY].

CRITICAL RULES:
1. [Rule 1]
2. [Rule 2]
...

TASK:
[Specific task for current stage]

CONTEXT:
Current stage: {stage}
Collected info: {collected_info}

RESPONSE FORMAT:
[Expected output format]
```

### Stage-Based Prompts

- **Greeting Prompt**: Introduces bot and explains purpose
- **Information Collector Prompt**: Asks for one piece of info, validates input
- **Tech Question Generator Prompt**: Generates relevant technical questions
- **Fallback Prompt**: Handles unclear/off-topic messages
- **Conclusion Prompt**: Summarizes and explains next steps
- **Exit Prompt**: Handles exit requests gracefully

## 🚀 Deployment

### Deploy to Streamlit Community Cloud

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repository, branch (main), and file (app.py)
   - Click "Advanced settings"
   - Add secrets:
     ```
     OPENAI_API_KEY = "sk-..."
     MODEL_NAME = "gpt-3.5-turbo"
     LLM_PROVIDER = "openai"
     ```
   - Click "Deploy"

3. **Access your app**
   - URL: `https://your-app-name.streamlit.app`

### Deploy to Hugging Face Spaces

1. **Create a Hugging Face account**
   - Go to [huggingface.co](https://huggingface.co)
   - Sign up for a free account

2. **Create a new Space**
   - Click "New Space"
   - Choose "Streamlit" SDK
   - Name your space (e.g., `talentscout-hiring-assistant`)

3. **Clone and setup**
   ```bash
   git clone https://huggingface.co/spaces/USERNAME/SPACE_NAME
   cd SPACE_NAME
   # Copy all project files here
   ```

4. **Add secrets**
   - Go to Space settings
   - Navigate to "Variables and secrets"
   - Add:
     - `OPENAI_API_KEY`
     - `MODEL_NAME`
     - `LLM_PROVIDER`

5. **Push to Hugging Face**
   ```bash
   git add .
   git commit -m "Deploy to Hugging Face"
   git push
   ```

6. **Access your app**
   - URL: `https://huggingface.co/spaces/USERNAME/SPACE_NAME`

## 🎯 Challenges & Solutions

### Challenge 1: Maintaining Conversation Context

**Problem**: LLM might forget previous conversation context.

**Solution**: 
- Implemented `ConversationManager` to track all messages
- Pass full conversation history to LLM in each request
- Store collected information separately for easy access

### Challenge 2: Input Validation

**Problem**: Users might provide invalid inputs in various formats.

**Solution**:
- Created comprehensive `Validator` class with specific validation rules
- Validate inputs before sending to LLM
- Provide clear, helpful error messages
- Support multiple input formats (e.g., "3 years" vs "3")

### Challenge 3: Generating Relevant Technical Questions

**Problem**: Questions should be relevant to candidate's tech stack.

**Solution**:
- Created question bank with 15+ technologies
- Use LLM to generate questions dynamically based on tech stack
- Pass previous Q&A pairs to maintain context
- Mix difficulty levels automatically

### Challenge 4: Handling Off-Topic Conversations

**Problem**: Users might try to chat about unrelated topics.

**Solution**:
- Implemented fallback prompts that gently redirect
- Check for exit keywords explicitly
- System prompts emphasize staying focused
- Validate inputs before processing

### Challenge 5: State Management in Streamlit

**Problem**: Streamlit reruns entire script on each interaction.

**Solution**:
- Use `st.session_state` to persist conversation state
- Initialize components only once
- Store conversation manager and LLM handler in session state

## 🔮 Future Improvements

### Potential Enhancements

1. **Export Conversation**
   - Download chat history as PDF/TXT
   - Include all Q&A pairs

2. **Sentiment Analysis**
   - Analyze candidate mood during conversation
   - Adapt bot tone based on sentiment

3. **Multi-language Support**
   - Detect user language automatically
   - Respond in same language
   - Use `langdetect` library

4. **Enhanced UI**
   - Animations for new messages
   - Typing indicator
   - Dark mode toggle
   - Sound effects (optional)

5. **Analytics Dashboard**
   - Conversation statistics
   - Time spent per stage
   - Most common tech stacks
   - Success rate metrics

6. **Database Integration**
   - Store candidate information in database
   - Retrieve conversation history
   - Generate reports

7. **Advanced Question Generation**
   - Difficulty level selection
   - Question categories (conceptual, practical, coding)
   - Adaptive questioning based on answers

## 🌐 Live Demo

### Streamlit Cloud
🔗 [Live Demo on Streamlit Cloud](https://your-app-name.streamlit.app)

### Hugging Face Spaces
🔗 [Live Demo on Hugging Face](https://huggingface.co/spaces/USERNAME/SPACE_NAME)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ for TalentScout Recruitment Agency**

*Last updated: 2024*


