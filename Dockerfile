FROM python:3.12

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

COPY alembic ./alembic

COPY alembic.ini .

COPY .env .

EXPOSE 8000

RUN alembic upgrade head

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
