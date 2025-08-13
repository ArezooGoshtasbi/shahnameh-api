from typing import List

from fastapi import APIRouter, Depends

from app.dependencies import get_chapter_service
from app.schemas.chapter import ChapterRead
from app.services.chapter_service import ChapterService

router = APIRouter(prefix="/chapters", tags=["chapters"])


@router.get("/", response_model=List[ChapterRead])
async def list_chapters(
    chapter_service: ChapterService = Depends(get_chapter_service),
):
    return await chapter_service.fetch_all_chapters()


# @router.get("/{chapter_id}", response_model=ChapterRead)
# async def get_chapter(
#     chapter_id: UUID, repo: ChapterService = Depends(get_chapter_service)
# ):
#     chapter = await repo.get_by_id(chapter_id)
#     if not chapter:
#         raise HTTPException(status_code=404, detail="Chapter not found")
#     return chapter
