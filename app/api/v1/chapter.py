from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends, Query

from app.dependencies import get_chapter_service
from app.schemas.chapter import ChapterRead
from app.services.chapter_service import ChapterService

router = APIRouter(prefix="/chapters", tags=["chapters"])


@router.get("/", response_model=List[ChapterRead])
async def list_chapters(
    title: str = Query(None, description="Filter chapters by title"),
    chapter_service: ChapterService = Depends(get_chapter_service),
):
    return await chapter_service.fetch_all_chapters(title=title)


@router.get("/{chapter_id}", response_model=ChapterRead)
async def get_chapter(
    chapter_id: str, chapter_service: ChapterService = Depends(get_chapter_service)
):
    chapter = await chapter_service.get_by_id(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter
