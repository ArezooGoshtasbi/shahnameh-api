from typing import TYPE_CHECKING, List, Optional
from uuid import UUID

from pydantic import BaseModel


class ChapterBase(BaseModel):
    title: str
    parent_id: Optional[UUID] = None
    order_in_parent: int


class ChapterRead(ChapterBase):
    id: UUID
    subchapters: Optional[List["ChapterRead"]] = []

    class Config:
        orm_mode = True  # allows automatic conversion from ORM model
        from_attributes = True


if TYPE_CHECKING:
    ChapterRead.update_forward_refs()
