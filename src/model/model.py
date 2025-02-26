from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TextIntentCreate(BaseModel):
    text_id: int
    expert_id: int
    intent_id: int
    is_true: bool = True


class TextIntentRead(BaseModel):
    text_intent_id: int
    text_id: int
    expert_id: int
    intent_id: int
    is_true: bool
    created_at: datetime

    class Config:
        from_attributes=True


class TextIntentUpdate(BaseModel):
    text_id: Optional[int] = None
    expert_id: Optional[int] = None
    intent_id: Optional[int] = None
    is_true: Optional[bool] = None


class ExpertCreate(BaseModel):
    name: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)


class ExpertRead(BaseModel):
    expert_id: int
    name: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True


class IntentTypeCreate(BaseModel):
    expert_id: int
    name: str
    frequency: Optional[int] = Field(default=0)


class IntentTypeUpdate(BaseModel):
    name: Optional[str] = None 
    frequency: Optional[int] = None


class IntentTypeRead(BaseModel):
    type_id: int
    expert_id: int
    name: Optional[str] = Field(default=None)
    frequency: Optional[int] = Field(default=None)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True

