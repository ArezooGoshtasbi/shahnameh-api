from uuid import UUID

from pydantic import BaseModel


class VerseBase(BaseModel):
    chapter_id: UUID
    order_in_chapter: int
    m1: str
    m2: str


class VerseRead(VerseBase):
    id: UUID

    class Config:
        orm_mode = True
        from_attributes = True
