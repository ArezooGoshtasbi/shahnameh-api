from app.repositories.chapter import IChapterRepository


class ChapterService:
    def __init__(self, repo: IChapterRepository):
        self.repo = repo

    async def fetch_all_chapters(self):
        return await self.repo.list()
