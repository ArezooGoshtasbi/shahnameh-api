from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ChapterMetadataBase(BaseModel):
    meter: Optional[str] = None
    poetic_form: Optional[str] = None
    verse_count: Optional[int] = None


class ChapterMetadataRead(ChapterMetadataBase):
    chapter_id: UUID

    class Config:
        orm_mode = True
        from_attributes = True
