from abc import ABC, abstractmethod


class IEmojiRepository(ABC):
    
    @abstractmethod
    def all(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, emoji: str) -> str | None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, emoji: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add(self, emoji: str) -> None:
        raise NotImplementedError()
