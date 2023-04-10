FROM python:3.10.9-buster

ENV POETRY_HOME /etc/poetry
ENV PATH $POETRY_HOME/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.4.0

RUN useradd -m -u 1000 app
USER 1000

WORKDIR /opt/chef_backend
COPY --chown=1000:1000 pyproject.toml poetry.lock /opt/chef_backend
COPY --chown=1000:1000 ./app /opt/chef_backend/app
RUN poetry install --no-root --no-interaction

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
