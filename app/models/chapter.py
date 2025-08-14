from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.chapter_metadata import ChapterMetadata  # noqa
from app.utils.model_uuid import uuid_column


class Chapter(Base):
    __tablename__ = "chapters"
    id = uuid_column(primary_key=True, nullable=False)
    title = Column(Text, nullable=False)
    parent_id = uuid_column(foreign_key="chapters.id")
    order_in_parent = Column(Integer, nullable=False)

    parent = relationship("Chapter", remote_side=[id], back_populates="subchapters")
    subchapters = relationship(
        "Chapter", back_populates="parent", cascade="all, delete-orphan"
    )
    chapter_metadata = relationship(
        "ChapterMetadata", uselist=False, back_populates="chapter"
    )
