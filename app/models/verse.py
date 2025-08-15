from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.utils.model_uuid import uuid_column


class Verse(Base):
    __tablename__ = "verses"
    id = uuid_column(primary_key=True, nullable=False)
    chapter_id = uuid_column(foreign_key="chapters.id", nullable=False)
    order_in_chapter = Column(Integer, nullable=False)
    m1 = Column(Text, nullable=False)
    m2 = Column(Text, nullable=False)

    chapter = relationship("Chapter", back_populates="verses")
