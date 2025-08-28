import uuid

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class Explanation(Base):
    __tablename__ = "explanations"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
    chapter_id = Column(UUID(as_uuid=True), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    verse_start = Column(Integer)
    verse_end = Column(Integer)
    embedding = Column(Vector(384))
