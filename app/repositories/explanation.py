from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.explanation import Explanation  # Import your ORM model
from app.schemas.explanation import ExplanationCreate, ExplanationRead


class IExplanationRepository(ABC):
    @abstractmethod
    async def create_explanation(
        self, explanation: ExplanationCreate, embedding: List[float]
    ) -> List[ExplanationRead]:
        pass

    @abstractmethod
    async def search(
        self, query_vec: List[float], limit: float = 0.5
    ) -> List[ExplanationRead]:
        pass


class ExplanationRepository(IExplanationRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def to_pgvector(v):
        return "[" + ",".join(f"{x:.6f}" for x in v) + "]"

    async def create_explanation(
        self, explanation: ExplanationCreate, embedding: List[float]
    ) -> ExplanationRead:
        new_explanation = Explanation(
            **explanation.model_dump(), embedding=embedding
        )
        self.db.add(new_explanation)
        await self.db.commit()
        await self.db.refresh(new_explanation)
        return new_explanation

    async def search(
        self, query_vec: List[float], limit: float = 1
    ) -> List[ExplanationRead]:
        vector_str = "[" + ",".join(str(float(x)) for x in query_vec) + "]"
        result = await self.db.execute(
            text(
                """
SELECT *, embedding <-> CAST(:query_vec AS vector) AS distance
FROM explanations
ORDER BY distance
LIMIT :limit
        """
            ),
            {"query_vec": vector_str, "limit": limit},
        )
        return result.fetchall()
