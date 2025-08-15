from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.chapter import ChapterRepository, IChapterRepository
from app.repositories.verse import IVerseRepository, VerseRepository
from app.services.chapter_service import ChapterService, IChapterService
from app.services.verse_service import IVerseService, VerseService


def get_chapter_repository(db: AsyncSession = Depends(get_db)) -> IChapterRepository:
    return ChapterRepository(db)


def get_verse_repository(db: AsyncSession = Depends(get_db)) -> IVerseRepository:
    return VerseRepository(db)


def get_chapter_service(
    repo: IChapterRepository = Depends(get_chapter_repository),
) -> IChapterService:
    return ChapterService(repo)


def get_verse_service(
    repo: IVerseRepository = Depends(get_verse_repository),
) -> IVerseService:
    return VerseService(repo)
