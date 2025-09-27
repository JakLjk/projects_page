FROM python:3.13

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y curl build-essential git && \
    curl -sSL https://install.python-poetry.org | python3 -


# Skonfiguruj użytkownika (UID/GID dopasujemy przy buildzie)
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID app && useradd -m -u $UID -g $GID app

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY --chown=app:app . .

COPY --chown=app:app --chmod=0755 entrypoint.sh /app/entrypoint.sh

RUN mkdir -p /NGINX_STATICFILES && chown -R app:app /NGINX_STATICFILES

USER app

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

