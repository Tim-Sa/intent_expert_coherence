import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import FastAPI

from src.database.async_session import AsyncSessionLocal
from src.model.model import ExpertCreate, ExpertRead
from src.api.main import app


@pytest.fixture
async def client():
    async with AsyncClient(
            transport=ASGITransport(app=app), 
            base_url="http://test"
        ) as client:
        
        yield client


@pytest.fixture
async def create_expert_data():
    return ExpertCreate(name="John Doe", phone="123-456-7890")


@pytest.mark.asyncio
async def test_create_expert(client, create_expert_data):
    response = await client.post("/experts/", json=create_expert_data.dict())
    assert response.status_code == 201
    assert response.json()["name"] == create_expert_data.name


@pytest.mark.asyncio
async def test_get_expert(client):
    response = await client.get("/experts/1")
    assert response.status_code == 200
    assert "name" in response.json()


@pytest.mark.asyncio
async def test_get_all_experts(client):
    response = await client.get("/experts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_expert(client, create_expert_data):
    expert_update = ExpertCreate(name="Jane Doe", phone="987-654-3210")
    response = await client.put("/experts/1", json=expert_update.dict())
    assert response.status_code == 200
    assert response.json()["name"] == expert_update.name


@pytest.mark.asyncio
async def test_delete_expert(client):
    response = await client.delete("/experts/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Expert deleted successfully"}


@pytest.mark.asyncio
async def test_get_expert_not_found(client):
    response = await client.get("/experts/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Expert not found"


@pytest.mark.asyncio
async def test_update_expert_not_found(client):
    expert_update = ExpertCreate(name="Non-existing Expert", phone="111-222-3333")
    response = await client.put("/experts/99999", json=expert_update.dict())
    assert response.status_code == 404
    assert response.json()["detail"] == "Expert not found"


@pytest.mark.asyncio
async def test_delete_expert_not_found(client):
    response = await client.delete("/experts/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Expert not found"
