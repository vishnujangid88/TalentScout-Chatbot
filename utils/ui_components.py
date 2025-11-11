"""
Reusable Streamlit UI components.
"""
import streamlit as st
from typing import Dict, Optional
from datetime import datetime


def display_chat_message(role: str, content: str, timestamp: Optional[str] = None) -> None:
    """
    Display a chat message in the Streamlit interface.
    
    Args:
        role: 'user' or 'assistant'
        content: Message content
        timestamp: Optional timestamp string
    """
    if role == "user":
        with st.chat_message("user"):
            st.write(content)
            if timestamp:
                st.caption(f"🕒 {_format_timestamp(timestamp)}")
    else:
        with st.chat_message("assistant"):
            st.write(content)
            if timestamp:
                st.caption(f"🕒 {_format_timestamp(timestamp)}")


def display_sidebar_info(candidate_info: Dict[str, Optional[str]]) -> None:
    """
    Display collected candidate information in the sidebar.
    
    Args:
        candidate_info: Dictionary of candidate information
    """
    st.sidebar.header("📋 Collected Information")
    
    field_labels = {
        "name": "👤 Full Name",
        "email": "📧 Email",
        "phone": "📱 Phone",
        "experience": "💼 Experience",
        "position": "🎯 Position",
        "location": "📍 Location",
        "tech_stack": "⚙️ Tech Stack"
    }
    
    for key, label in field_labels.items():
        value = candidate_info.get(key)
        if value:
            st.sidebar.markdown(f"**{label}**")
            st.sidebar.write(value)
            st.sidebar.markdown("---")
        else:
            st.sidebar.markdown(f"**{label}**")
            st.sidebar.write("_Not collected yet_")
            st.sidebar.markdown("---")


def display_progress_indicator(current_stage: str, current_step: int, total_steps: int) -> None:
    """
    Display progress indicator in sidebar.
    
    Args:
        current_stage: Current conversation stage name
        current_step: Current step number
        total_steps: Total number of steps
    """
    st.sidebar.header("📊 Progress")
    
    # Progress bar
    progress = current_step / total_steps if total_steps > 0 else 0
    st.sidebar.progress(progress)
    st.sidebar.write(f"**Step {current_step} of {total_steps}**")
    st.sidebar.caption(f"Current: {current_stage.replace('_', ' ').title()}")
    st.sidebar.markdown("---")


def apply_custom_css() -> None:
    """Load and apply custom CSS styling."""
    import os
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css")
    try:
        if os.path.exists(css_path):
            with open(css_path, "r", encoding="utf-8") as f:
                css = f.read()
                st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except Exception:
        # CSS file not found or error reading, use default styling
        pass


def display_error_message(message: str) -> None:
    """
    Display an error message.
    
    Args:
        message: Error message to display
    """
    st.error(f"⚠️ {message}")


def display_success_message(message: str) -> None:
    """
    Display a success message.
    
    Args:
        message: Success message to display
    """
    st.success(f"✅ {message}")


def display_info_message(message: str) -> None:
    """
    Display an info message.
    
    Args:
        message: Info message to display
    """
    st.info(f"ℹ️ {message}")


def display_tech_stack_reference() -> None:
    """Display tech stack reference in sidebar."""
    from config.settings import SUPPORTED_TECH_STACKS
    
    with st.sidebar.expander("📚 Supported Tech Stacks"):
        for category, techs in SUPPORTED_TECH_STACKS.items():
            st.markdown(f"**{category}**")
            st.write(", ".join(techs[:10]))  # Show first 10
            if len(techs) > 10:
                st.caption(f"... and {len(techs) - 10} more")
            st.markdown("---")


def _format_timestamp(timestamp: str) -> str:
    """
    Format timestamp for display.
    
    Args:
        timestamp: ISO format timestamp string
        
    Returns:
        Formatted timestamp string
    """
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%H:%M:%S")
    except Exception:
        return timestamp


def display_loading_indicator() -> None:
    """Display a loading indicator."""
    st.spinner("🤔 Thinking...")


def create_reset_button() -> bool:
    """
    Create a reset button in the sidebar.
    
    Returns:
        True if button was clicked
    """
    return st.sidebar.button("🔄 Reset Conversation", type="primary", use_container_width=True)

