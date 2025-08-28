from abc import ABC, abstractmethod

from sentence_transformers import SentenceTransformer

from app.repositories.explanation import IExplanationRepository
from app.schemas.explanation import ExplanationCreate


class IExplanationService(ABC):
    @abstractmethod
    async def create_explanation(
        self,
        explanation: ExplanationCreate,
    ):
        pass

    @abstractmethod
    async def search(self, query: str):
        pass


class ExplanationService(IExplanationService):
    def __init__(self, repo: IExplanationRepository):
        self.repo = repo
        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

    async def create_explanation(
        self,
        explanation: ExplanationCreate,
    ):
        vec = self.model.encode([explanation.text], normalize_embeddings=True)[
            0
        ]

        return await self.repo.create_explanation(
            explanation=explanation,
            embedding=vec.tolist(),
        )

    async def search(self, query: str):
        query_vec = self.model.encode([query], normalize_embeddings=True)[
            0
        ].tolist()
        results = await self.repo.search(query_vec)
        return results
