from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies import Container
from app.schemas.verse import VerseRead
from app.services.verse_service import IVerseService

router = APIRouter(prefix="/verses", tags=["verses"])


@router.get("/search", response_model=List[VerseRead])
@inject
async def list_verses_by_substrings(
    substrings: List[str] = Query(
        ...,
        description="Filter verses by substrings (at least one required)",
        min_items=1,
        example=["ایران", "رستم"],
    ),
    verse_service: IVerseService = Depends(Provide[Container.verse_service]),
):
    if not substrings:
        raise HTTPException(
            status_code=422, detail="At least one substring must be provided."
        )
    return await verse_service.list_by_substrings(substrings=substrings)


@router.get("/{verse_id}", response_model=VerseRead)
@inject
async def get_verse_by_id(
    verse_id: str,
    verse_service: IVerseService = Depends(Provide[Container.verse_service]),
):
    verse = await verse_service.get_by_id(verse_id)
    if not verse:
        raise HTTPException(status_code=404, detail="Verse not found")
    return verse
