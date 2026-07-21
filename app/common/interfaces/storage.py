#app/common/interfaces/storage.py
from abc import ABC, abstractmethod
from fastapi import UploadFile


class Storage(ABC):
    @abstractmethod
    async def save(self, file: UploadFile) -> tuple[str, int]:
        pass

    @abstractmethod
    async def delete(self, filename: str) -> None:
        pass
