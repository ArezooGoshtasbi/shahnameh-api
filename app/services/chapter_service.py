from app.repositories.chapter import IChapterRepository


class ChapterService:
    def __init__(self, repo: IChapterRepository):
        self.repo = repo

    async def fetch_all_chapters(self):
        return await self.repo.list()

    async def get_by_id(self, chapter_id: str):
        return await self.repo.get_by_id(chapter_id)
