"""
Setup verification script to check if all dependencies are installed correctly.
"""
import sys

def check_python_version():
    """Check if Python version is 3.9 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9+ is required. Current version:", sys.version)
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_dependencies():
    """Check if all required packages are installed."""
    required_packages = [
        "streamlit",
        "openai",
        "groq",
        "email_validator",
        "phonenumbers",
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == "email_validator":
                __import__("email_validator")
            elif package == "phonenumbers":
                __import__("phonenumbers")
            else:
                __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_api_keys():
    """Check if API keys are configured."""
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    openai_key = os.getenv("OPENAI_API_KEY", "")
    groq_key = os.getenv("GROQ_API_KEY", "")
    
    if openai_key and openai_key != "sk-your-key-here":
        print("✅ OpenAI API key is configured")
        return True
    elif groq_key and groq_key != "your-groq-key-here":
        print("✅ Groq API key is configured")
        return True
    else:
        print("⚠️  No API key found in environment variables")
        print("   Please set OPENAI_API_KEY or GROQ_API_KEY in .env file")
        return False

def check_project_structure():
    """Check if project structure is correct."""
    import os
    
    required_files = [
        "app.py",
        "requirements.txt",
        "config/settings.py",
        "prompts/system_prompts.py",
        "utils/llm_handler.py",
        "utils/conversation_manager.py",
        "utils/validators.py",
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} is missing")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def main():
    """Run all checks."""
    print("=" * 50)
    print("TalentScout Hiring Assistant - Setup Verification")
    print("=" * 50)
    print()
    
    all_checks_passed = True
    
    print("1. Checking Python version...")
    if not check_python_version():
        all_checks_passed = False
    print()
    
    print("2. Checking dependencies...")
    deps_ok, missing = check_dependencies()
    if not deps_ok:
        all_checks_passed = False
        print(f"\n   Install missing packages with: pip install {' '.join(missing)}")
    print()
    
    print("3. Checking API keys...")
    check_api_keys()
    print()
    
    print("4. Checking project structure...")
    if not check_project_structure():
        all_checks_passed = False
    print()
    
    print("=" * 50)
    if all_checks_passed:
        print("✅ All checks passed! You're ready to run the app.")
        print("\n   Run: streamlit run app.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
    print("=" * 50)

if __name__ == "__main__":
    main()


