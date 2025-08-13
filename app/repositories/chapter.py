from typing import List, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.chapter import Chapter
from app.schemas.chapter import ChapterRead


class IChapterRepository:
    async def get_by_id(self, chapter_id: UUID) -> Optional[ChapterRead]:
        raise NotImplementedError

    async def list(self, title: str = None) -> List[ChapterRead]:
        raise NotImplementedError


class ChapterRepository(IChapterRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def _sort_subchapters(self, chapter: ChapterRead):
        chapter.subchapters.sort(key=lambda x: x.order_in_parent)
        for sub in chapter.subchapters:
            self._sort_subchapters(sub)

    async def get_by_id(self, chapter_id: UUID) -> ChapterRead:
        query = (
            select(Chapter)
            .where(Chapter.id == chapter_id)  # noqa: E711
            # load sub chapters too:
            .options(
                selectinload(Chapter.subchapters).selectinload(Chapter.subchapters)
            )
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def list(self, title: str = None) -> List[ChapterRead]:
        query = (
            select(Chapter)
            # "is" not gonna work here
            .where(Chapter.parent_id == None)  # noqa: E711
            # load sub chapters too:
            .options(
                selectinload(Chapter.subchapters).selectinload(Chapter.subchapters)
            )
            .order_by(Chapter.order_in_parent)
        )
        if title:
            query = query.where(Chapter.title.ilike(f"%{title}%"))
        result = await self.db.execute(query)
        return result.scalars().all()
