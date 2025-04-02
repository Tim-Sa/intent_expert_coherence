FROM python:3.12

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

COPY alembic ./alembic

COPY alembic.ini .

COPY .local.env .

EXPOSE 8000

COPY wait-for-it.sh /usr/local/bin/wait-for-it

RUN chmod +x /usr/local/bin/wait-for-it

CMD ["sh", "-c", "wait-for-it $PSQL_DB_HOST:$PSQL_DB_PORT -- alembic upgrade head && uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload"]
