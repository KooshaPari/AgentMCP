"""Stub schemas module - placeholder for undefined schema types used in test_models.py."""

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel as PydanticBaseModel, field_validator
from models.enums import ExecutionLanguage


class MessageSchema(PydanticBaseModel):
    """Stub message schema."""
    role: str
    content: str


class ContextSchema(PydanticBaseModel):
    """Stub context schema."""
    user_id: str
    session_id: Optional[str] = None


class ExecuteCodeRequest(PydanticBaseModel):
    """Execute code request schema."""
    code: str
    language: Union[ExecutionLanguage, str] = ExecutionLanguage.PYTHON
    timeout: int = 30
    max_output_size: int = 10000
    context: Dict[str, Any] = {}

    @field_validator('language', mode='before')
    @classmethod
    def validate_language(cls, v):
        if isinstance(v, str):
            return ExecutionLanguage(v)
        return v

    @field_validator('timeout')
    @classmethod
    def validate_timeout(cls, v):
        if v < 1 or v > 300:
            raise ValueError("timeout must be between 1 and 300 seconds")
        return v

    class Config:
        validate_assignment = True


class ExecuteCodeResponse(PydanticBaseModel):
    """Stub execute code response schema."""
    execution_id: str
    status: str = "success"
    result: Optional[Any] = None
    error: Optional[str] = None
    output: Optional[str] = None
    variables: List[str] = []
    execution_time_ms: Optional[float] = None
