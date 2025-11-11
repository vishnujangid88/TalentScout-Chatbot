"""
Conversation state management and stage tracking.
"""
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from config.settings import (
    ConversationStage,
    STAGE_SEQUENCE,
    EXIT_KEYWORDS,
    get_min_questions,
    get_max_questions
)


class ConversationManager:
    """Manages conversation state, stages, and candidate information."""
    
    def __init__(self):
        """Initialize conversation manager."""
        self.stage = ConversationStage.GREETING
        self.candidate_info: Dict[str, Optional[str]] = {
            "name": None,
            "email": None,
            "phone": None,
            "experience": None,
            "position": None,
            "location": None,
            "tech_stack": None
        }
        self.tech_questions_asked: int = 0
        self.tech_questions_answers: List[Tuple[str, str]] = []  # List of (question, answer) tuples
        self.conversation_history: List[Dict[str, str]] = []  # List of {role, content, timestamp}
        self.start_time: datetime = datetime.now()
        self.current_question: Optional[str] = None
        self.total_questions_to_ask: int = 0
        self.tech_stack_list: List[str] = []
    
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to conversation history.
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
        """
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_next_stage(self) -> ConversationStage:
        """Get the next stage in the conversation sequence."""
        try:
            current_index = STAGE_SEQUENCE.index(self.stage)
            if current_index < len(STAGE_SEQUENCE) - 1:
                return STAGE_SEQUENCE[current_index + 1]
            return ConversationStage.ENDED
        except ValueError:
            return ConversationStage.ENDED
    
    def move_to_next_stage(self) -> None:
        """Move to the next stage in the sequence."""
        self.stage = self.get_next_stage()
        
        # Special handling for technical questions stage
        if self.stage == ConversationStage.TECHNICAL_QUESTIONS:
            self._prepare_technical_questions()
    
    def _prepare_technical_questions(self) -> None:
        """Prepare technical questions based on tech stack."""
        if not self.candidate_info.get("tech_stack"):
            return
        
        # Parse tech stack
        tech_stack_str = self.candidate_info["tech_stack"]
        self.tech_stack_list = [t.strip() for t in tech_stack_str.split(",")]
        
        # Determine number of questions (3-5)
        import random
        min_q = get_min_questions()
        max_q = get_max_questions()
        self.total_questions_to_ask = random.randint(min_q, max_q)
        self.tech_questions_asked = 0
        self.tech_questions_answers = []
    
    def update_candidate_info(self, field: str, value: str) -> None:
        """
        Update a specific field in candidate information.
        
        Args:
            field: Field name (name, email, phone, etc.)
            value: Field value
        """
        if field in self.candidate_info:
            self.candidate_info[field] = value
    
    def is_info_complete(self) -> bool:
        """
        Check if all required information has been collected.
        
        Returns:
            True if all fields are filled
        """
        required_fields = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]
        return all(self.candidate_info.get(field) for field in required_fields)
    
    def get_collected_info_summary(self) -> str:
        """
        Get a formatted summary of collected information.
        
        Returns:
            Formatted string summary
        """
        summary = "Collected Information:\n"
        field_labels = {
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "experience": "Years of Experience",
            "position": "Desired Position",
            "location": "Current Location",
            "tech_stack": "Tech Stack"
        }
        
        for key, label in field_labels.items():
            value = self.candidate_info.get(key)
            if value:
                summary += f"- {label}: {value}\n"
        
        return summary
    
    def check_exit_keyword(self, message: str) -> bool:
        """
        Check if message contains an exit keyword.
        
        Args:
            message: User message to check
            
        Returns:
            True if exit keyword found
        """
        message_lower = message.lower().strip()
        return any(keyword in message_lower for keyword in EXIT_KEYWORDS)
    
    def get_stage_prompt_context(self) -> Dict[str, str]:
        """
        Get context information for current stage.
        
        Returns:
            Dictionary with stage context
        """
        return {
            "stage": self.stage.value,
            "collected_info": self.candidate_info,
            "needed_info": self._get_needed_info_for_stage()
        }
    
    def _get_needed_info_for_stage(self) -> str:
        """Get description of what information is needed for current stage."""
        stage_info_map = {
            ConversationStage.COLLECT_NAME: "Full Name",
            ConversationStage.COLLECT_EMAIL: "Email Address",
            ConversationStage.COLLECT_PHONE: "Phone Number",
            ConversationStage.COLLECT_EXPERIENCE: "Years of Experience",
            ConversationStage.COLLECT_POSITION: "Desired Position",
            ConversationStage.COLLECT_LOCATION: "Current Location",
            ConversationStage.COLLECT_TECH_STACK: "Tech Stack",
            ConversationStage.TECHNICAL_QUESTIONS: "Answer to technical question",
            ConversationStage.CONCLUSION: "None - conversation ending",
            ConversationStage.ENDED: "None - conversation ended"
        }
        return stage_info_map.get(self.stage, "Unknown")
    
    def add_technical_question_answer(self, question: str, answer: str) -> None:
        """
        Add a question-answer pair for technical questions.
        
        Args:
            question: Technical question asked
            answer: Candidate's answer
        """
        self.tech_questions_answers.append((question, answer))
        self.tech_questions_asked += 1
    
    def has_more_technical_questions(self) -> bool:
        """Check if there are more technical questions to ask."""
        return self.tech_questions_asked < self.total_questions_to_ask
    
    def get_current_question_number(self) -> int:
        """Get current question number (1-based)."""
        return self.tech_questions_asked + 1
    
    def reset(self) -> None:
        """Reset conversation manager to initial state."""
        self.__init__()
    
    def get_progress(self) -> Tuple[int, int]:
        """
        Get conversation progress.
        
        Returns:
            Tuple of (current_step, total_steps)
        """
        try:
            current_index = STAGE_SEQUENCE.index(self.stage)
            total_steps = len(STAGE_SEQUENCE) - 1  # Exclude ENDED stage
            return current_index, total_steps
        except ValueError:
            return 0, len(STAGE_SEQUENCE) - 1


