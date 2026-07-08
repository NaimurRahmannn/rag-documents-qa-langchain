CHUNK_SIZE=500
CHUNK_OVERLAP=100
TOP_K=3
EMBEDDING_MODEL="all-MiniLM-L6-v2"
CHROMA_PERSIST_DIR="chroma_db"
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"

settings = Settings()

GOOGLE_API_KEY = settings.GOOGLE_API_KEY
GEMINI_MODEL = settings.GEMINI_MODEL