"""
Application settings and configuration constants.
"""
import os
import streamlit as st
from enum import Enum
from typing import Dict, List


class ConversationStage(Enum):
    """Enumeration of conversation stages."""
    GREETING = "greeting"
    COLLECT_NAME = "collect_name"
    COLLECT_EMAIL = "collect_email"
    COLLECT_PHONE = "collect_phone"
    COLLECT_EXPERIENCE = "collect_experience"
    COLLECT_POSITION = "collect_position"
    COLLECT_LOCATION = "collect_location"
    COLLECT_TECH_STACK = "collect_tech_stack"
    TECHNICAL_QUESTIONS = "technical_questions"
    CONCLUSION = "conclusion"
    ENDED = "ended"


# Exit keywords that will end the conversation
EXIT_KEYWORDS = ["exit", "quit", "bye", "goodbye", "stop", "end", "cancel", "terminate"]

# Stage sequence for conversation flow
STAGE_SEQUENCE = [
    ConversationStage.GREETING,
    ConversationStage.COLLECT_NAME,
    ConversationStage.COLLECT_EMAIL,
    ConversationStage.COLLECT_PHONE,
    ConversationStage.COLLECT_EXPERIENCE,
    ConversationStage.COLLECT_POSITION,
    ConversationStage.COLLECT_LOCATION,
    ConversationStage.COLLECT_TECH_STACK,
    ConversationStage.TECHNICAL_QUESTIONS,
    ConversationStage.CONCLUSION,
    ConversationStage.ENDED,
]

# Supported tech stacks organized by category
SUPPORTED_TECH_STACKS = {
    "Frontend": [
        "React", "Angular", "Vue.js", "JavaScript", "TypeScript", "HTML", "CSS",
        "SASS", "SCSS", "Tailwind CSS", "Bootstrap", "Next.js", "Nuxt.js",
        "Svelte", "jQuery", "Redux", "MobX", "Webpack", "Vite"
    ],
    "Backend": [
        "Python", "Django", "Flask", "FastAPI", "Node.js", "Express", "Java",
        "Spring Boot", "C#", ".NET", "ASP.NET", "Ruby", "Ruby on Rails",
        "PHP", "Laravel", "Go", "Golang", "Rust", "Scala", "Kotlin"
    ],
    "Mobile": [
        "React Native", "Flutter", "Swift", "Kotlin", "Java", "Objective-C",
        "Xamarin", "Ionic", "Cordova", "Android", "iOS"
    ],
    "Database": [
        "PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite", "Oracle",
        "SQL Server", "Cassandra", "Elasticsearch", "DynamoDB", "Firebase",
        "Neo4j", "CouchDB", "MariaDB"
    ],
    "DevOps": [
        "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Jenkins", "GitLab CI",
        "GitHub Actions", "Terraform", "Ansible", "Chef", "Puppet", "Vagrant",
        "Linux", "Bash", "Shell Scripting", "Nginx", "Apache"
    ],
    "Data Science": [
        "Pandas", "NumPy", "TensorFlow", "PyTorch", "Scikit-learn", "Keras",
        "Matplotlib", "Seaborn", "Jupyter", "R", "SQL", "Apache Spark",
        "Hadoop", "Tableau", "Power BI", "MLflow", "XGBoost", "LightGBM"
    ],
    "Other": [
        "Git", "REST API", "GraphQL", "Microservices", "CI/CD", "Agile",
        "Scrum", "JIRA", "Confluence", "Postman", "Swagger", "OAuth",
        "JWT", "WebSocket", "gRPC"
    ]
}

# Flatten tech stack list for easier searching
ALL_TECH_STACKS = []
for category, techs in SUPPORTED_TECH_STACKS.items():
    ALL_TECH_STACKS.extend(techs)


def get_api_key() -> str:
    """
    Get API key from Streamlit secrets or environment variables.
    Priority: Streamlit secrets > Environment variables
    """
    # Try Streamlit secrets first
    try:
        if hasattr(st, 'secrets'):
            provider = get_llm_provider()
            if provider == "groq":
                api_key = st.secrets.get("GROQ_API_KEY") or st.secrets.get("API_KEY")
            else:
                api_key = st.secrets.get("OPENAI_API_KEY") or st.secrets.get("API_KEY")
            if api_key:
                return api_key
    except Exception:
        pass
    
    # Fall back to environment variables
    provider = os.getenv("LLM_PROVIDER", "openai")
    if provider == "groq":
        return os.getenv("GROQ_API_KEY", "")
    else:
        return os.getenv("OPENAI_API_KEY", "")


def get_llm_provider() -> str:
    """Get LLM provider from secrets or environment variables."""
    try:
        if hasattr(st, 'secrets'):
            provider = st.secrets.get("LLM_PROVIDER")
            if provider:
                return provider.lower()
    except Exception:
        pass
    
    return os.getenv("LLM_PROVIDER", "openai").lower()


def get_model_name() -> str:
    """Get model name from secrets or environment variables."""
    try:
        if hasattr(st, 'secrets'):
            model = st.secrets.get("MODEL_NAME")
            if model:
                return model
    except Exception:
        pass
    
    provider = get_llm_provider()
    if provider == "groq":
        # Try common currently available models - update based on Groq's current offerings
        # Common options: llama-3.3-70b-versatile, llama-3.1-8b-instant, mixtral-8x7b-32768
        return os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
    else:
        return os.getenv("MODEL_NAME", "gpt-3.5-turbo")


def get_app_title() -> str:
    """Get app title from secrets or environment variables."""
    try:
        if hasattr(st, 'secrets'):
            title = st.secrets.get("APP_TITLE")
            if title:
                return title
    except Exception:
        pass
    
    return os.getenv("APP_TITLE", "TalentScout Hiring Assistant")


def get_company_name() -> str:
    """Get company name from secrets or environment variables."""
    try:
        if hasattr(st, 'secrets'):
            company = st.secrets.get("COMPANY_NAME")
            if company:
                return company
    except Exception:
        pass
    
    return os.getenv("COMPANY_NAME", "TalentScout")


def get_max_questions() -> int:
    """Get maximum number of technical questions."""
    try:
        if hasattr(st, 'secrets'):
            max_q = st.secrets.get("MAX_QUESTIONS")
            if max_q:
                return int(max_q)
    except Exception:
        pass
    
    return int(os.getenv("MAX_QUESTIONS", "5"))


def get_min_questions() -> int:
    """Get minimum number of technical questions."""
    try:
        if hasattr(st, 'secrets'):
            min_q = st.secrets.get("MIN_QUESTIONS")
            if min_q:
                return int(min_q)
    except Exception:
        pass
    
    return int(os.getenv("MIN_QUESTIONS", "3"))


