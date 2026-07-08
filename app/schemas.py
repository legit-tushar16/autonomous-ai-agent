# schemas.py
from pydantic import BaseModel, Field
from typing import List

class AgentRequest(BaseModel):
    request: str = Field(..., description="The natural language business document request from the user.")

class Task(BaseModel):
    id: int = Field(..., description="Unique sequential ID for the task.")
    title: str = Field(..., description="The title of the section to generate.")
    description: str = Field(..., description="Detailed instructions on what contents this specific section needs to cover.")

class PlanResponse(BaseModel):
    document_title: str = Field(..., description="A professional title for the overall business document.")
    tasks: List[Task] = Field(..., description="The collection of structured sequential sections needed to build this document.")

class ReflectionResult(BaseModel):
    is_approved: bool = Field(..., description="True if the draft content satisfies all quality and professional formatting constraints.")
    critique: str = Field(..., description="If not approved, explicitly document what corrections are needed.")