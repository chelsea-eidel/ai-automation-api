from fastapi import APIRouter, HTTPException
from app.models import (
    SummarizeRequest,
    SummarizeResponse,
    TaskExtractionRequest,
    TaskExtractionResponse,
    StructuredExtractionRequest,
    StructuredExtractionResponse,
)
from app.llm_service import LLMService

router = APIRouter()
_llm_service: LLMService | None = None


def get_llm_service() -> LLMService:
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest) -> SummarizeResponse:
    try:
        summary = get_llm_service().summarize_text(request.text)
        return SummarizeResponse(summary=summary)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/extract/tasks", response_model=TaskExtractionResponse)
def extract_tasks(request: TaskExtractionRequest) -> TaskExtractionResponse:
    try:
        result = get_llm_service().extract_tasks(request.text)
        return TaskExtractionResponse(**result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/extract/structured", response_model=StructuredExtractionResponse)
def extract_structured(
    request: StructuredExtractionRequest,
) -> StructuredExtractionResponse:
    try:
        result = get_llm_service().extract_structured(
            text=request.text,
            schema_description=request.schema_description,
        )
        return StructuredExtractionResponse(data=result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc