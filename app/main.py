from fastapi import FastAPI

from app.api.v1.chapter import router as chapter_router
from app.api.v1.verse import router as verse_router
from app.dependencies import Container

# from app.core.database import get_db

app = FastAPI()

container = Container()


# @app.on_event("startup")
# async def startup():
#     await get_db().connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await get_db().disconnect()


app.include_router(chapter_router, prefix="/api/v1")
app.include_router(verse_router, prefix="/api/v1")
