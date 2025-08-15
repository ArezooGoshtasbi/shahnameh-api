from dependency_injector import containers, providers

from app.core.database import AsyncSessionLocal
from app.repositories.chapter import ChapterRepository
from app.repositories.verse import VerseRepository
from app.services.chapter_service import ChapterService
from app.services.verse_service import VerseService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.api.v1.chapter", "app.api.v1.verse"]
    )

    db = providers.Factory(lambda: AsyncSessionLocal())
    chapter_repository = providers.Factory(ChapterRepository, db=db)
    verse_repository = providers.Factory(VerseRepository, db=db)
    chapter_service = providers.Factory(ChapterService, repo=chapter_repository)
    verse_service = providers.Factory(VerseService, repo=verse_repository)


# Usage in endpoints:
# from app.dependencies import Container
# container = Container()
# chapter_service = container.chapter_service(db=db)
