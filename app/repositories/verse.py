from typing import List, Optional
from uuid import UUID

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.verse import Verse
from app.schemas.verse import VerseRead


class IVerseRepository:
    async def get_by_id(self, verse_id: UUID) -> Optional[VerseRead]:
        raise NotImplementedError

    async def list_by_substrings(self, substrings: List[str]) -> List[VerseRead]:
        raise NotImplementedError


class VerseRepository(IVerseRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, verse_id: UUID) -> VerseRead:
        query = (
            select(Verse).where(Verse.id == verse_id)  # noqa: E711
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def list_by_substrings(self, substrings: List[str]) -> List[VerseRead]:
        conditions = [
            (Verse.m1.ilike(f"%{s}%") | Verse.m2.ilike(f"%{s}%")) for s in substrings
        ]
        query = select(Verse).where(and_(*conditions))
        result = await self.db.execute(query)
        return result.scalars().all()
