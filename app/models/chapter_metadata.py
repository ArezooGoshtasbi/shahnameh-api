from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class ChapterMetadata(Base):
    __tablename__ = "chapter_metadata"
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), primary_key=True)
    meter = Column(Text)
    poetic_form = Column(Text)
    verse_count = Column(Integer)

    chapter = relationship("Chapter", back_populates="chapter_metadata")
