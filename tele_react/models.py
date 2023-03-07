from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class EmojiModel(Base):
    __tablename__ = 'emojis'
    emoji = Column(String, primary_key=True, nullable=False)


class ChatModel(Base):
    __tablename__ = 'chats'
    chat = Column(String, primary_key=True, nullable=False)
