from abc import ABC, abstractmethod
from typing import List

from app.repositories.verse import IVerseRepository


class IVerseService(ABC):
    @abstractmethod
    async def list_by_substrings(self, substrings: List[str]):
        pass

    @abstractmethod
    async def get_by_id(self, verse_id: str):
        pass

    @abstractmethod
    async def list_by_chapter_id(self, chapter_id: str):
        pass


class VerseService(IVerseService):
    def __init__(self, repo: IVerseRepository):
        self.repo = repo

    async def list_by_substrings(self, substrings: List[str]):
        return await self.repo.list_by_substrings(substrings=substrings)

    async def get_by_id(self, verse_id: str):
        return await self.repo.get_by_id(verse_id)

    async def list_by_chapter_id(self, chapter_id: str):
        return await self.repo.list_by_chapter_id(chapter_id=chapter_id)
