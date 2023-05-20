FROM python:{{cookiecutter.python_version}} as base

RUN pip install poetry
RUN poetry virtualenvs.options.always-copy true

FROM base as python-base
COPY ./poetry.lock ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-root --without dev

FROM python-base as dev

COPY --from=python-base /app/.venv /app/.venv
COPY . /app/
RUN poetry install

FROM dev as test

ENTRYPOINT ["poetry", "run", "pytest"]

CMD ["--cov"]
