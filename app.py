"""
TalentScout Hiring Assistant Chatbot - Main Streamlit Application
"""
import streamlit as st
from config.settings import (
    ConversationStage,
    get_app_title,
    get_company_name,
    get_min_questions,
    get_max_questions
)
from utils.conversation_manager import ConversationManager
from utils.llm_handler import LLMHandler
from utils.validators import Validator
from utils.ui_components import (
    display_chat_message,
    display_sidebar_info,
    display_progress_indicator,
    apply_custom_css,
    display_error_message,
    display_tech_stack_reference,
    create_reset_button
)


# Page configuration
try:
    st.set_page_config(
        page_title=get_app_title(),
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded"
    )
except Exception:
    # Page config already set, ignore
    pass

# Apply custom CSS
apply_custom_css()

# Initialize session state
if "conversation_manager" not in st.session_state:
    st.session_state.conversation_manager = ConversationManager()

if "llm_handler" not in st.session_state:
    try:
        st.session_state.llm_handler = LLMHandler()
    except Exception as e:
        st.error(f"Failed to initialize LLM handler: {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "awaiting_answer" not in st.session_state:
    st.session_state.awaiting_answer = False

if "current_question" not in st.session_state:
    st.session_state.current_question = None


def initialize_conversation():
    """Initialize conversation with greeting."""
    if not st.session_state.initialized:
        try:
            greeting = st.session_state.llm_handler.generate_greeting()
            st.session_state.conversation_manager.add_message("assistant", greeting)
            st.session_state.messages.append({
                "role": "assistant",
                "content": greeting,
                "timestamp": st.session_state.conversation_manager.conversation_history[-1]["timestamp"]
            })
            st.session_state.initialized = True
        except Exception as e:
            display_error_message(f"Failed to generate greeting: {str(e)}")


def validate_and_process_input(user_input: str) -> tuple:
    """
    Validate user input based on current stage and process it.
    
    Returns:
        Tuple of (is_valid, processed_value, error_message)
    """
    stage = st.session_state.conversation_manager.stage
    validator = Validator()
    
    if stage == ConversationStage.COLLECT_NAME:
        is_valid, result = validator.validate_name(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_EMAIL:
        is_valid, result = validator.validate_email(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_PHONE:
        is_valid, result = validator.validate_phone(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_EXPERIENCE:
        is_valid, result = validator.validate_experience(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_POSITION:
        is_valid, result = validator.validate_position(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_LOCATION:
        is_valid, result = validator.validate_location(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.COLLECT_TECH_STACK:
        is_valid, result = validator.validate_tech_stack(user_input)
        return is_valid, result, "" if is_valid else result
    
    elif stage == ConversationStage.TECHNICAL_QUESTIONS:
        # For technical questions, any non-empty input is valid
        if user_input.strip():
            return True, user_input.strip(), ""
        return False, "", "Please provide an answer to the question."
    
    return True, user_input, ""


def get_field_name_for_stage(stage: ConversationStage) -> str:
    """Get field name for current stage."""
    field_map = {
        ConversationStage.COLLECT_NAME: "name",
        ConversationStage.COLLECT_EMAIL: "email",
        ConversationStage.COLLECT_PHONE: "phone",
        ConversationStage.COLLECT_EXPERIENCE: "experience",
        ConversationStage.COLLECT_POSITION: "position",
        ConversationStage.COLLECT_LOCATION: "location",
        ConversationStage.COLLECT_TECH_STACK: "tech_stack"
    }
    return field_map.get(stage, "")


def handle_user_message(user_input: str):
    """Handle user message and generate bot response."""
    cm = st.session_state.conversation_manager
    llm = st.session_state.llm_handler
    
    # Check for exit keywords
    if cm.check_exit_keyword(user_input):
        exit_message = llm.generate_exit_message()
        cm.add_message("user", user_input)
        cm.add_message("assistant", exit_message)
        cm.stage = ConversationStage.ENDED
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": cm.conversation_history[-2]["timestamp"]
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": exit_message,
            "timestamp": cm.conversation_history[-1]["timestamp"]
        })
        return
    
    # Handle different stages
    if cm.stage == ConversationStage.TECHNICAL_QUESTIONS:
        # Handle technical question answer
        if st.session_state.current_question:
            # Save answer
            cm.add_technical_question_answer(st.session_state.current_question, user_input)
            cm.add_message("user", user_input)
            
            # Check if more questions
            if cm.has_more_technical_questions():
                # Generate next question
                question_num = cm.get_current_question_number()
                tech_stack = cm.candidate_info.get("tech_stack", "")
                question = llm.generate_technical_question(
                    tech_stack=tech_stack,
                    question_number=question_num,
                    num_questions=cm.total_questions_to_ask,
                    previous_qa=cm.tech_questions_answers
                )
                st.session_state.current_question = question
                cm.add_message("assistant", question)
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_input,
                    "timestamp": cm.conversation_history[-2]["timestamp"]
                })
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": question,
                    "timestamp": cm.conversation_history[-1]["timestamp"]
                })
            else:
                # All questions answered, move to conclusion
                cm.move_to_next_stage()
                conclusion = llm.generate_conclusion(cm.candidate_info)
                cm.add_message("assistant", conclusion)
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_input,
                    "timestamp": cm.conversation_history[-2]["timestamp"]
                })
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": conclusion,
                    "timestamp": cm.conversation_history[-1]["timestamp"]
                })
                st.session_state.current_question = None
        return
    
    # Validate input for information collection stages
    is_valid, processed_value, error_msg = validate_and_process_input(user_input)
    
    if not is_valid:
        # Invalid input - show error and ask again
        cm.add_message("user", user_input)
        error_response = f"I'm sorry, but that doesn't seem right. {error_msg} Please try again."
        cm.add_message("assistant", error_response)
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": cm.conversation_history[-2]["timestamp"]
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": error_response,
            "timestamp": cm.conversation_history[-1]["timestamp"]
        })
        return
    
    # Valid input - save and move to next stage
    field_name = get_field_name_for_stage(cm.stage)
    if field_name:
        cm.update_candidate_info(field_name, processed_value)
    
    cm.add_message("user", user_input)
    
    # Move to next stage
    cm.move_to_next_stage()
    
    # Generate response for next stage
    if cm.stage == ConversationStage.TECHNICAL_QUESTIONS:
        # Generate first technical question
        tech_stack = cm.candidate_info.get("tech_stack", "")
        question_num = 1
        question = llm.generate_technical_question(
            tech_stack=tech_stack,
            question_number=question_num,
            num_questions=cm.total_questions_to_ask,
            previous_qa=[]
        )
        st.session_state.current_question = question
        cm.add_message("assistant", question)
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": cm.conversation_history[-2]["timestamp"]
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": question,
            "timestamp": cm.conversation_history[-1]["timestamp"]
        })
    elif cm.stage == ConversationStage.CONCLUSION:
        # Generate conclusion
        conclusion = llm.generate_conclusion(cm.candidate_info)
        cm.add_message("assistant", conclusion)
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": cm.conversation_history[-2]["timestamp"]
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": conclusion,
            "timestamp": cm.conversation_history[-1]["timestamp"]
        })
    else:
        # Generate response for next information collection stage
        stage_context = cm.get_stage_prompt_context()
        response = llm.generate_info_collector_response(
            stage=stage_context["stage"],
            user_message=user_input,
            collected_info=stage_context["collected_info"]
        )
        cm.add_message("assistant", response)
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": cm.conversation_history[-2]["timestamp"]
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": cm.conversation_history[-1]["timestamp"]
        })


# Sidebar
st.sidebar.title(f"💼 {get_company_name()}")
st.sidebar.markdown("**Hiring Assistant Chatbot**")
st.sidebar.markdown("---")

# Progress indicator
current_step, total_steps = st.session_state.conversation_manager.get_progress()
display_progress_indicator(
    st.session_state.conversation_manager.stage.value,
    current_step,
    total_steps
)

# Collected information
display_sidebar_info(st.session_state.conversation_manager.candidate_info)

# Tech stack reference
display_tech_stack_reference()

# Reset button
if create_reset_button():
    st.session_state.conversation_manager.reset()
    st.session_state.messages = []
    st.session_state.initialized = False
    st.session_state.current_question = None
    st.rerun()

# Main chat interface
st.title(f"💼 {get_app_title()}")
st.markdown("Welcome! I'm here to help you through our initial screening process.")

# Initialize conversation
initialize_conversation()

# Display chat history
for message in st.session_state.messages:
    display_chat_message(
        message["role"],
        message["content"],
        message.get("timestamp")
    )

# User input
if st.session_state.conversation_manager.stage != ConversationStage.ENDED:
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        with st.spinner("🤔 Processing..."):
            handle_user_message(user_input)
            st.rerun()
else:
    st.info("💬 Conversation has ended. Click 'Reset Conversation' in the sidebar to start over.")

# Footer
st.markdown("---")
st.caption(f"© 2024 {get_company_name()}. All rights reserved.")

