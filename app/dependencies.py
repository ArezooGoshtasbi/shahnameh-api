from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.chapter import ChapterRepository
from app.services.chapter_service import ChapterService


def get_chapter_repository(db: AsyncSession = Depends(get_db)) -> ChapterRepository:
    return ChapterRepository(db)


def get_chapter_service(
    user_repo: ChapterRepository = Depends(get_chapter_repository),
) -> ChapterService:
    return ChapterService(user_repo)
