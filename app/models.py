from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1)


class SummarizeResponse(BaseModel):
    summary: str


class TaskItem(BaseModel):
    title: str
    due_date: Optional[str] = None
    priority: Optional[str] = None


class TaskExtractionRequest(BaseModel):
    text: str = Field(..., min_length=1)


class TaskExtractionResponse(BaseModel):
    tasks: List[TaskItem]


class StructuredExtractionRequest(BaseModel):
    text: str = Field(..., min_length=1)
    schema_description: str = Field(
        ...,
        description="Human-readable description of the desired JSON output schema"
    )


class StructuredExtractionResponse(BaseModel):
    data: Dict[str, Any]