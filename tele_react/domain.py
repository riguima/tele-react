from abc import ABC, abstractmethod


class IEmojiRepository(ABC):
    
    @abstractmethod
    def all(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, emoji: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add(self, emoji: str) -> None:
        raise NotImplementedError()


class IChatRepository(ABC):
    
    @abstractmethod
    def all(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, chat: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add(self, chat: str) -> None:
        raise NotImplementedError()
