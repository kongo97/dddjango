FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      libxml2-dev \
      libxslt1-dev \
      libffi-dev \
      curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./poetry.lock /app/
COPY ./pyproject.toml /app/

RUN poetry install --no-dev --no-ansi

COPY ./src /app/

COPY ./.entrypoint /tmp/.entrypoint
RUN chmod +x /tmp/.entrypoint

EXPOSE 8000

ENTRYPOINT ["/tmp/.entrypoint"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
