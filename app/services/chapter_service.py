from abc import ABC, abstractmethod

from app.repositories.chapter import IChapterRepository


class IChapterService(ABC):
    @abstractmethod
    async def fetch_all_chapters(self, title: str = None):
        pass

    @abstractmethod
    async def get_by_id(self, chapter_id: str):
        pass


class ChapterService(IChapterService):
    def __init__(self, repo: IChapterRepository):
        self.repo = repo

    async def fetch_all_chapters(self, title: str = None):
        return await self.repo.list(title=title)

    async def get_by_id(self, chapter_id: str):
        return await self.repo.get_by_id(chapter_id)
