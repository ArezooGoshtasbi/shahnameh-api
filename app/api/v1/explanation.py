from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies import Container
from app.schemas.explanation import (
    ExplanationCreate,
    ExplanationRead,
)
from app.services.explanation import IExplanationService

router = APIRouter(prefix="/explanations", tags=["explanations"])


@router.post("/", response_model=ExplanationRead)
@inject
async def create_explanation_with_chunks(
    explanation: ExplanationCreate,
    explanation_service: IExplanationService = Depends(
        Provide[Container.explanation_service]
    ),
):
    result = await explanation_service.create_explanation(explanation)
    if not result:
        raise HTTPException(
            status_code=400, detail="Failed to create explanation."
        )
    return result


@router.get("/search", response_model=List[ExplanationRead])
@inject
async def search(
    query: str = Query(None, description="Queries chapter explanations"),
    explanation_service: IExplanationService = Depends(
        Provide[Container.explanation_service]
    ),
):
    return await explanation_service.search(query=query)
