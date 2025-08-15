from http.client import HTTPException
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from app.dependencies import Container
from app.schemas.chapter import ChapterRead
from app.schemas.verse import VerseRead
from app.services.chapter_service import IChapterService
from app.services.verse_service import IVerseService

router = APIRouter(prefix="/chapters", tags=["chapters"])


@router.get("/", response_model=List[ChapterRead])
@inject
async def list_chapters(
    title: str = Query(None, description="Filter chapters by title"),
    chapter_service: IChapterService = Depends(Provide[Container.chapter_service]),
):
    return await chapter_service.fetch_all_chapters(title=title)


@router.get("/{chapter_id}", response_model=ChapterRead)
@inject
async def get_chapter(
    chapter_id: str,
    chapter_service: IChapterService = Depends(Provide[Container.chapter_service]),
):
    chapter = await chapter_service.get_by_id(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter


@router.get("/{chapter_id}/verses", response_model=List[VerseRead])
@inject
async def list_chapter_verses(
    chapter_id: str,
    verse_service: IVerseService = Depends(Provide[Container.verse_service]),
):
    return await verse_service.list_by_chapter_id(chapter_id)
