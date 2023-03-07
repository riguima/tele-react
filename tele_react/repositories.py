from domain import IEmojiRepository, IChatRepository
from database import Session
from models import EmojiModel, ChatModel


class EmojiRepository(IEmojiRepository):
    
    def all(self) -> list[str]:
        with Session() as session:
            return [m.emoji for m in session.query(EmojiModel).all()]

    def delete(self, emoji: str) -> None:
        with Session() as session:
            model = session.query(EmojiModel).get(emoji)
            if model:
                session.delete(model)
                session.commit()

    def add(self, emoji: str) -> None:
        with Session() as session:
            session.add(EmojiModel(emoji=emoji))
            session.commit()


class ChatRepository(IChatRepository):
    
    def all(self) -> list[str]:
        with Session() as session:
            return [m.name for m in session.query(ChatModel).all()]

    def add(self, chat: str) -> None:
        with Session() as session:
            session.add(ChatModel(chat=chat))
            session.commit()

    def delete(self, chat: str) -> None:
        with Session() as session:
            model = session.query(ChatModel).get(chat)
            if model:
                session.delete(model)
                session.commit()
