"""
Input validation functions for candidate information.
"""
import re
from typing import Tuple
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from phonenumbers import NumberParseException


class Validator:
    """Static methods for validating candidate information."""
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """
        Validate full name.
        
        Rules:
        - Minimum 2 characters
        - Only letters, spaces, periods, hyphens, apostrophes
        
        Args:
            name: Name string to validate
            
        Returns:
            Tuple of (is_valid, normalized_name or error_message)
        """
        if not name or not isinstance(name, str):
            return False, "Name cannot be empty."
        
        name = name.strip()
        
        if len(name) < 2:
            return False, "Name must be at least 2 characters long."
        
        # Allow letters, spaces, periods, hyphens, apostrophes
        pattern = r"^[a-zA-Z\s\.\-\']+$"
        if not re.match(pattern, name):
            return False, "Name can only contain letters, spaces, periods, hyphens, and apostrophes."
        
        # Normalize: remove extra spaces, capitalize properly
        name = " ".join(name.split())
        return True, name.title()
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """
        Validate email address.
        
        Args:
            email: Email string to validate
            
        Returns:
            Tuple of (is_valid, normalized_email or error_message)
        """
        if not email or not isinstance(email, str):
            return False, "Email cannot be empty."
        
        email = email.strip()
        
        try:
            # Validate and normalize email
            validation = validate_email(email, check_deliverability=False)
            normalized_email = validation.email
            return True, normalized_email
        except EmailNotValidError as e:
            return False, f"Invalid email format: {str(e)}"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """
        Validate phone number in international format.
        
        Args:
            phone: Phone string to validate
            
        Returns:
            Tuple of (is_valid, formatted_phone or error_message)
        """
        if not phone or not isinstance(phone, str):
            return False, "Phone number cannot be empty."
        
        phone = phone.strip()
        
        # Remove common separators for parsing
        phone_clean = re.sub(r'[\s\-\(\)\.]', '', phone)
        
        try:
            # Try to parse the phone number
            # Default to US if no country code provided
            parsed_number = phonenumbers.parse(phone, None)
            
            # Check if it's a valid number
            if not phonenumbers.is_valid_number(parsed_number):
                return False, "Invalid phone number. Please provide a valid international phone number with country code (e.g., +1 234 567 8900)."
            
            # Format in international format
            formatted = phonenumbers.format_number(
                parsed_number,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            return True, formatted
        except NumberParseException as e:
            return False, f"Invalid phone number format. Please provide an international phone number with country code (e.g., +1 234 567 8900). Error: {str(e)}"
    
    @staticmethod
    def validate_experience(experience: str) -> Tuple[bool, str]:
        """
        Validate years of experience.
        
        Accepts formats like "3 years", "3", "three years", etc.
        Range: 0-50 years
        
        Args:
            experience: Experience string to validate
            
        Returns:
            Tuple of (is_valid, years_string or error_message)
        """
        if not experience or not isinstance(experience, str):
            return False, "Experience cannot be empty."
        
        experience = experience.strip().lower()
        
        # Remove common words
        experience = re.sub(r'\s*(years?|yrs?|year|yr)\s*', '', experience)
        
        # Try to extract number
        numbers = re.findall(r'\d+', experience)
        
        if not numbers:
            # Try word-to-number conversion for common cases
            word_to_num = {
                'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
                'fourteen': 14, 'fifteen': 15, 'twenty': 20, 'thirty': 30
            }
            for word, num in word_to_num.items():
                if word in experience:
                    years = num
                    break
            else:
                return False, "Please provide a valid number of years (0-50)."
        else:
            years = int(numbers[0])
        
        # Validate range
        if years < 0 or years > 50:
            return False, "Experience must be between 0 and 50 years."
        
        return True, str(years)
    
    @staticmethod
    def validate_position(position: str) -> Tuple[bool, str]:
        """
        Validate desired position.
        
        Rules:
        - Minimum 3 characters
        
        Args:
            position: Position string to validate
            
        Returns:
            Tuple of (is_valid, normalized_position or error_message)
        """
        if not position or not isinstance(position, str):
            return False, "Position cannot be empty."
        
        position = position.strip()
        
        if len(position) < 3:
            return False, "Position must be at least 3 characters long."
        
        # Normalize: remove extra spaces
        position = " ".join(position.split())
        return True, position
    
    @staticmethod
    def validate_location(location: str) -> Tuple[bool, str]:
        """
        Validate current location.
        
        Rules:
        - Minimum 2 characters
        
        Args:
            location: Location string to validate
            
        Returns:
            Tuple of (is_valid, normalized_location or error_message)
        """
        if not location or not isinstance(location, str):
            return False, "Location cannot be empty."
        
        location = location.strip()
        
        if len(location) < 2:
            return False, "Location must be at least 2 characters long."
        
        # Normalize: remove extra spaces
        location = " ".join(location.split())
        return True, location
    
    @staticmethod
    def validate_tech_stack(tech_stack: str) -> Tuple[bool, str]:
        """
        Validate tech stack.
        
        Rules:
        - Minimum 2 characters
        
        Args:
            tech_stack: Tech stack string to validate
            
        Returns:
            Tuple of (is_valid, normalized_tech_stack or error_message)
        """
        if not tech_stack or not isinstance(tech_stack, str):
            return False, "Tech stack cannot be empty."
        
        tech_stack = tech_stack.strip()
        
        if len(tech_stack) < 2:
            return False, "Tech stack must be at least 2 characters long."
        
        # Normalize: remove extra spaces, handle comma-separated values
        tech_list = [t.strip() for t in tech_stack.split(',') if t.strip()]
        normalized = ", ".join(tech_list)
        
        return True, normalized


