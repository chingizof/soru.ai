"""
Configuration module for Soru.ai application.
Manages environment variables and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration class."""
    
    # Google Gemini API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    # Hugging Face API Configuration
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
    HUGGINGFACE_API_URL = os.getenv(
        "HUGGINGFACE_API_URL",
        "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
    )
    
    # Application Settings
    APP_NAME = os.getenv("APP_NAME", "lahacks_24")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate that all required configuration values are set.
        
        Returns:
            bool: True if all required values are present, False otherwise
        """
        required_vars = [
            ("GOOGLE_API_KEY", cls.GOOGLE_API_KEY),
            ("HUGGINGFACE_API_KEY", cls.HUGGINGFACE_API_KEY),
        ]
        
        missing_vars = [name for name, value in required_vars if not value]
        
        if missing_vars:
            print(f"⚠️  Warning: Missing required environment variables: {', '.join(missing_vars)}")
            print("Please check your .env file or environment configuration.")
            return False
        
        return True
    
    @classmethod
    def get_headers(cls) -> dict:
        """
        Get HTTP headers for Hugging Face API requests.
        
        Returns:
            dict: Headers dictionary with authorization token
        """
        return {"Authorization": f"Bearer {cls.HUGGINGFACE_API_KEY}"}


# Validate configuration on import
if not Config.validate():
    print("\n📝 To fix this:")
    print("1. Copy .env.example to .env")
    print("2. Add your API keys to the .env file")
    print("3. Restart the application\n")

