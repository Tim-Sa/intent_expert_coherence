from fastapi import FastAPI

from src.api.routes.entity import (
    expert_router, intent_type_router, intent_router
)
from src.api.routes.user import user_router

app = FastAPI(title="Expert API")

app.include_router(expert_router)
app.include_router(intent_type_router)
app.include_router(intent_router)

app.include_router(user_router)

