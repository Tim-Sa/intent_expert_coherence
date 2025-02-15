from pydantic import BaseModel
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
        orm_mode = True


class TextIntentUpdate(BaseModel):
    text_id: Optional[int] = None
    expert_id: Optional[int] = None
    intent_id: Optional[int] = None
    is_true: Optional[bool] = None
