import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Токен бота
    API_TOKEN: str = os.environ["API_TOKEN"]
    if not API_TOKEN.strip():
        raise ValueError("API_TOKEN must not be empty!")