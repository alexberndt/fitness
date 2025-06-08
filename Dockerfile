FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install the application dependencies.
WORKDIR /app

COPY uv.lock pyproject.toml ./

RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY fitness ./fitness

CMD ["/app/.venv/bin/uvicorn", "fitness.main:app", "--port", "80", "--host", "0.0.0.0"]