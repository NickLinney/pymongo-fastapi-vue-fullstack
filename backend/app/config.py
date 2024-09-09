import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI MongoDB App"
    PROJECT_VERSION: str = "1.0.0"
    MONGO_DETAILS: str = os.getenv("MONGO_DETAILS", "mongodb://mongodb:27017")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()
