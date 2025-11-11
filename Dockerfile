FROM python:3.13.9-alpine3.22

RUN pip install --no-cache-dir uv==0.9.5

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-cache

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
