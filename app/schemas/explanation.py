from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ExplanationBase(BaseModel):
    chunk_index: int
    text: str
    verse_start: Optional[int] = None
    verse_end: Optional[int] = None


class ExplanationCreate(ExplanationBase):
    chapter_id: UUID


class ExplanationRead(ExplanationBase):
    id: UUID
    chapter_id: UUID

    class Config:
        orm_mode = True
        from_attributes = True
