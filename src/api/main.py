from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.entity import (
    expert_router, intent_type_router, intent_router
)

app = FastAPI(title="Expert API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expert_router)
app.include_router(intent_type_router)
app.include_router(intent_router)

