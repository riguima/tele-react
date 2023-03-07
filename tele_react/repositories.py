from domain import IRepository
from database import Session
from models import EmojiModel, ChatModel


class EmojiRepository(IRepository):
    
    def all(self) -> list[str]:
        with Session() as session:
            return [m.emoji for m in session.query(EmojiModel).all()]

    def delete(self, key: str) -> None:
        with Session() as session:
            model = session.query(EmojiModel).get(key)
            if model:
                session.delete(model)
                session.commit()

    def add(self, key: str) -> None:
        with Session() as session:
            session.add(EmojiModel(emoji=key))
            session.commit()


class ChatRepository(IRepository):
    
    def all(self) -> list[str]:
        with Session() as session:
            return [m.chat for m in session.query(ChatModel).all()]

    def add(self, key: str) -> None:
        with Session() as session:
            session.add(ChatModel(chat=key))
            session.commit()

    def delete(self, key: str) -> None:
        with Session() as session:
            model = session.query(ChatModel).get(key)
            if model:
                session.delete(model)
                session.commit()
