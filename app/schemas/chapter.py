from typing import TYPE_CHECKING, List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.chapter_metadata import ChapterMetadataRead
from app.schemas.verse import VerseRead


class ChapterBase(BaseModel):
    title: str
    parent_id: Optional[UUID] = None
    order_in_parent: int


class ChapterRead(ChapterBase):
    id: UUID
    subchapters: Optional[List["ChapterRead"]] = []
    chapter_metadata: Optional[ChapterMetadataRead] = None
    verses: Optional[List[VerseRead]] = []

    class Config:
        orm_mode = True  # allows automatic conversion from ORM model
        from_attributes = True


if TYPE_CHECKING:
    ChapterRead.update_forward_refs()
