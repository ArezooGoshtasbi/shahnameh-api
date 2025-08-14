import os

from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


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
