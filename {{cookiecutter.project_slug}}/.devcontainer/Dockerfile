ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN pip install poetry
USER vscode
RUN poetry config virtualenvs.create true && poetry config virtualenvs.in-project true