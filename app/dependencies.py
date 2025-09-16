from dependency_injector import containers, providers

from app.core.database import AsyncSessionLocal
from app.repositories.chapter import ChapterRepository
from app.repositories.explanation import ExplanationRepository
from app.repositories.verse import VerseRepository
from app.services.chapter_service import ChapterService
from app.services.explanation import ExplanationService
from app.services.verse_service import VerseService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.chapter",
            "app.api.v1.verse",
            "app.api.v1.explanation",
        ]
    )

    db = providers.Factory(lambda: AsyncSessionLocal())
    chapter_repository = providers.Factory(ChapterRepository, db=db)
    verse_repository = providers.Factory(VerseRepository, db=db)
    explanation_repository = providers.Factory(ExplanationRepository, db=db)
    chapter_service = providers.Factory(
        ChapterService, repo=chapter_repository
    )
    verse_service = providers.Factory(VerseService, repo=verse_repository)
    explanation_service = providers.Factory(
        ExplanationService, repo=explanation_repository
    )
