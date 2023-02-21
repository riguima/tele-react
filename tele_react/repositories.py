from domain import IEmojiRepository
from database import Session
from models import EmojiModel


class EmojiRepository(IEmojiRepository):
    
    def all(self) -> list[str]:
        with Session() as session:
            return [m.emoji for m in session.query(EmojiModel).all()]

    def get(self, emoji: str) -> str | None:
        with Session() as session:
            model = session.query(EmojiModel).get(emoji)
            return model.emoji if model else None

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
