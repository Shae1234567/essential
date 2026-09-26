import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ASSISTANT_NAME: str = os.getenv("ASSISTANT_NAME", "EssentialCore")
    API_KEY: str = os.getenv("API_KEY", "")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

config = Config()
