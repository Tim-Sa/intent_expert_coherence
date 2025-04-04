import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from httpx import ASGITransport, AsyncClient

from src.api.main import app
from src.api.utils import get_db
import src.model.entity as py_model
import src.database.model.entity as db_model

DATABASE_URL = "sqlite+aiosqlite:///:memory:"  

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@pytest.fixture(scope="module")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(db_model.Base.metadata.create_all)
    yield  
    async with engine.begin() as conn:
        await conn.run_sync(db_model.Base.metadata.drop_all) 


@pytest.fixture()
async def db_session(setup_database):
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture()
async def client(db_session):
    async def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db 
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test") as client:
        yield client 


@pytest.fixture
async def create_expert_data():
    return py_model.ExpertCreate(name="John Doe", phone="123-456-7890")


@pytest.mark.asyncio
async def test_create_expert(client, create_expert_data):
    response = await client.post("/experts/", json=create_expert_data.model_dump())
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
async def test_update_expert(client):
    expert_update = py_model.ExpertCreate(name="Jane Doe", phone="987-654-3210")
    response = await client.put("/experts/1", json=expert_update.model_dump())
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
    expert_update = py_model.ExpertCreate(name="Non-existing Expert", phone="111-222-3333")
    response = await client.put("/experts/99999", json=expert_update.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "Expert not found"


@pytest.mark.asyncio
async def test_delete_expert_not_found(client):
    response = await client.delete("/experts/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Expert not found"


@pytest.fixture
async def create_intent_type_data():
    return py_model.IntentTypeCreate(name="General Inquiry", expert_id=1)


@pytest.mark.asyncio
async def test_create_intent_type(client, create_intent_type_data):
    response = await client.post("/intent-types/", json=create_intent_type_data.model_dump())
    assert response.status_code == 201
    assert response.json()["name"] == create_intent_type_data.name


@pytest.mark.asyncio
async def test_get_intent_type(client):
    response = await client.get("/intent-types/1")
    assert response.status_code == 200
    assert "name" in response.json()


@pytest.mark.asyncio
async def test_get_all_intent_types(client):
    response = await client.get("/intent-types/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_intent_type(client):
    intent_type_update = py_model.IntentTypeUpdate(name="Updated Inquiry")
    response = await client.put("/intent-types/1", json=intent_type_update.model_dump())
    assert response.status_code == 200
    assert response.json()["name"] == intent_type_update.name


@pytest.mark.asyncio
async def test_delete_intent_type(client):
    response = await client.delete("/intent-types/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Intent Type deleted successfully"}


@pytest.mark.asyncio
async def test_get_intent_type_not_found(client):
    response = await client.get("/intent-types/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent Type not found"


@pytest.mark.asyncio
async def test_update_intent_type_not_found(client):
    intent_type_update = py_model.IntentTypeUpdate(name="Non-existing Intent Type")
    response = await client.put("/intent-types/99999", json=intent_type_update.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent Type not found"


@pytest.mark.asyncio
async def test_delete_intent_type_not_found(client):
    response = await client.delete("/intent-types/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent Type not found"


@pytest.fixture
async def create_intent_data():
    return py_model.IntentCreate(expert_id=1, name="Sample Intent", type_id=1, frequency=10, k_fleiss_coherence=0.85)


@pytest.mark.asyncio
async def test_create_intent(client, create_intent_data):
    response = await client.post("/intents/", json=create_intent_data.model_dump())
    assert response.status_code == 201
    assert response.json()["name"] == create_intent_data.name
    assert response.json()["expert_id"] == create_intent_data.expert_id


@pytest.mark.asyncio
async def test_get_intent(client):
    response = await client.get("/intents/1")
    assert response.status_code == 200
    assert "name" in response.json()


@pytest.mark.asyncio
async def test_get_all_intents(client):
    response = await client.get("/intents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_intent(client):
    intent_update = py_model.IntentUpdate(name="Updated Intent", frequency=15)
    response = await client.put("/intents/1", json=intent_update.model_dump())
    assert response.status_code == 200
    assert response.json()["name"] == intent_update.name
    assert response.json()["frequency"] == intent_update.frequency


@pytest.mark.asyncio
async def test_delete_intent(client):
    response = await client.delete("/intents/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Intent deleted successfully"}


@pytest.mark.asyncio
async def test_get_intent_not_found(client):
    response = await client.get("/intents/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent not found"


@pytest.mark.asyncio
async def test_update_intent_not_found(client):
    intent_update = py_model.IntentUpdate(name="Non-existing Intent")
    response = await client.put("/intents/99999", json=intent_update.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent not found"


@pytest.mark.asyncio
async def test_delete_intent_not_found(client):
    response = await client.delete("/intents/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Intent not found"