from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(Text, nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), nullable=True)
    order_in_parent = Column(Integer, nullable=False)

    parent = relationship("Chapter", remote_side=[id], back_populates="subchapters")
    subchapters = relationship(
        "Chapter", back_populates="parent", cascade="all, delete-orphan"
    )
