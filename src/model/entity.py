from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from src.model.base import BaseModelConfig


class TextIntentCreate(BaseModel):
    text_id: int
    expert_id: int
    intent_id: int
    is_true: bool = True


class TextIntentRead(BaseModelConfig):
    text_intent_id: int
    text_id: int
    expert_id: int
    intent_id: int
    is_true: bool
    created_at: datetime


class TextIntentUpdate(BaseModel):
    text_id: Optional[int] = None
    expert_id: Optional[int] = None
    intent_id: Optional[int] = None
    is_true: Optional[bool] = None


class ExpertCreate(BaseModel):
    name: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)


class ExpertRead(BaseModelConfig):
    expert_id: int
    name: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class IntentTypeCreate(BaseModel):
    expert_id: int
    name: str
    frequency: Optional[int] = Field(default=0)


class IntentTypeUpdate(BaseModel):
    name: Optional[str] = None 
    frequency: Optional[int] = None


class IntentTypeRead(BaseModelConfig):
    type_id: int
    expert_id: int
    name: Optional[str] = Field(default=None)
    frequency: Optional[int] = Field(default=None)
    created_at: datetime
    updated_at: datetime


class IntentCreate(BaseModel):
    expert_id: int
    name: Optional[str] = Field(default=None)
    type_id: int
    frequency: Optional[int] = Field(default=None)
    k_fleiss_coherence: Optional[float] = Field(default=None)


class IntentUpdate(BaseModel):
    name: Optional[str] = None
    frequency: Optional[int] = None
    k_fleiss_coherence: Optional[float] = None


class IntentRead(BaseModelConfig):
    intent_id: int
    expert_id: int
    name: Optional[str] = Field(default=None)
    type_id: int
    frequency: Optional[int] = Field(default=None)
    k_fleiss_coherence: Optional[float] = Field(default=None)
    created_at: datetime
    updated_at: datetime
