"""
LLM handler for OpenAI and Groq API integration.
"""
import os
from typing import List, Dict, Optional
from config.settings import get_api_key, get_llm_provider, get_model_name


class LLMHandler:
    """Handler for LLM API calls (OpenAI and Groq)."""
    
    def __init__(self):
        """Initialize LLM handler with API key and provider."""
        self.api_key = get_api_key()
        self.provider = get_llm_provider().lower()
        self.model_name = get_model_name()
        
        if not self.api_key:
            raise ValueError(
                "API key not found. Please set OPENAI_API_KEY or GROQ_API_KEY "
                "in environment variables or Streamlit secrets."
            )
        
        # Initialize client based on provider
        if self.provider == "groq":
            try:
                from groq import Groq
                self.client = Groq(api_key=self.api_key)
            except ImportError:
                raise ImportError(
                    "Groq library not installed. Install it with: pip install groq"
                )
        else:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                raise ImportError(
                    "OpenAI library not installed. Install it with: pip install openai"
                )
    
    def generate_response(
        self,
        messages: List[Dict[str, str]],
        system_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> str:
        """
        Generate response from LLM.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            system_prompt: System prompt to guide the conversation
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens in response
            
        Returns:
            Generated response text
        """
        try:
            # Prepare messages with system prompt
            formatted_messages = [{"role": "system", "content": system_prompt}]
            formatted_messages.extend(messages)
            
            if self.provider == "groq":
                # Groq API call
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=formatted_messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            else:
                # OpenAI API call
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=formatted_messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            error_msg = str(e)
            # Don't expose API keys in error messages
            if "api" in error_msg.lower() and "key" in error_msg.lower():
                return "I'm having trouble connecting to the AI service. Please check your API key configuration."
            return f"I encountered an error: {error_msg}. Please try again."
    
    def generate_technical_question(
        self,
        tech_stack: str,
        question_number: int,
        num_questions: int,
        previous_qa: Optional[List[tuple]] = None
    ) -> str:
        """
        Generate a technical question based on tech stack.
        
        Args:
            tech_stack: Comma-separated list of technologies
            question_number: Current question number (1-based)
            num_questions: Total number of questions
            previous_qa: List of (question, answer) tuples from previous questions
            
        Returns:
            Generated technical question
        """
        from prompts.system_prompts import get_tech_question_generator_prompt
        
        system_prompt = get_tech_question_generator_prompt(
            tech_stack=tech_stack,
            question_number=question_number,
            num_questions=num_questions,
            previous_qa=previous_qa
        )
        
        # Use conversation history if available
        messages = []
        if previous_qa:
            for q, a in previous_qa:
                messages.append({"role": "user", "content": f"Q: {q}"})
                messages.append({"role": "assistant", "content": f"A: {a}"})
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.8,  # Slightly higher for more creative questions
            max_tokens=200
        )
    
    def generate_greeting(self) -> str:
        """Generate initial greeting message."""
        from prompts.system_prompts import get_greeting_prompt
        
        system_prompt = get_greeting_prompt()
        messages = []
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=150
        )
    
    def generate_info_collector_response(
        self,
        stage: str,
        user_message: str,
        collected_info: Dict[str, str]
    ) -> str:
        """
        Generate response for information collection stage.
        
        Args:
            stage: Current conversation stage
            user_message: User's input message
            collected_info: Dictionary of collected information
            
        Returns:
            Bot response
        """
        from prompts.system_prompts import get_information_collector_prompt
        
        system_prompt = get_information_collector_prompt(stage, collected_info)
        messages = [{"role": "user", "content": user_message}]
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=200
        )
    
    def generate_fallback_response(
        self,
        stage: str,
        user_message: str,
        needed_info: Optional[str] = None
    ) -> str:
        """
        Generate fallback response for unclear/off-topic inputs.
        
        Args:
            stage: Current conversation stage
            user_message: User's input message
            needed_info: What information is currently needed
            
        Returns:
            Bot response redirecting user
        """
        from prompts.system_prompts import get_fallback_prompt
        
        system_prompt = get_fallback_prompt(stage, needed_info)
        messages = [{"role": "user", "content": user_message}]
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=150
        )
    
    def generate_conclusion(self, collected_info: Dict[str, str]) -> str:
        """
        Generate conclusion message.
        
        Args:
            collected_info: Dictionary of all collected information
            
        Returns:
            Conclusion message
        """
        from prompts.system_prompts import get_conclusion_prompt
        
        system_prompt = get_conclusion_prompt(collected_info)
        messages = []
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=300
        )
    
    def generate_exit_message(self) -> str:
        """Generate exit message."""
        from prompts.system_prompts import get_exit_prompt
        
        system_prompt = get_exit_prompt()
        messages = []
        
        return self.generate_response(
            messages=messages,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=150
        )


