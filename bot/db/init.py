from db.engine import engine, SessionLocal
from config import Settings
from db.db_model import Base, LogChats

settings = Settings()

def init():
    Base.metadata.create_all(bind=engine)
    for chat_id in settings.CHAT_TO_SEND_RESULT:
        LogChats.add_chat(chat_id, SessionLocal())
