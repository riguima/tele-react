from abc import ABC, abstractmethod


class IRepository(ABC):
    
    @abstractmethod
    def all(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, key: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add(self, key: str) -> None:
        raise NotImplementedError()
