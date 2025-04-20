# settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY: str = os.getenv("API_KEY")
    MAX_LENGTH: int = 10000
    SAFETY_CONFIG: dict = {
        "harassment": "block",
        "hate_speech": "block",
        "sexually_explicit": "block",
        "dangerous_content": "block",
    }
    GENERATION_CONFIG: dict = {
        "temperature": 0.7,
        "top_p": 0.8,
        "top_k": 40,
        "max_output_tokens": 1024,
    }

settings = Settings()