import os

from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# since sqlite uses text for UUIDs,
# we need to check the type of the db and provide the correct column type
def uuid_column(*, primary_key=False, foreign_key=None, nullable=True):
    db_url = os.getenv("DATABASE_URL", "")
    if db_url.startswith("postgresql"):
        coltype = PG_UUID(as_uuid=True)
    else:
        coltype = Text
    args = [coltype]
    kwargs = {"primary_key": primary_key, "nullable": nullable}
    if foreign_key:
        args.append(ForeignKey(foreign_key))
    return Column(*args, **kwargs)


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
