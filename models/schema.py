from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID

class CandidateEmbedding(BaseModel):
    id: UUID
    candidate_id: UUID
    embedding: List[float]
    content: str
    created_at: str

class JobEmbedding(BaseModel):
    id: UUID
    job_id: UUID
    embedding: List[float]
    content: str
    created_at: str

class ChatRequest(BaseModel):
    job_id: UUID
    candidate_ids: List[UUID]
    question: str
    context_type: Optional[str] = None 

    model_config = ConfigDict(arbitrary_types_allowed=True)
