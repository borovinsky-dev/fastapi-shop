FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.1 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy
WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --no-dev --no-install-project --locked
COPY app ./app
RUN uv sync --no-dev --locked

EXPOSE 8000
CMD ["uv", "run", "--no-dev", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
