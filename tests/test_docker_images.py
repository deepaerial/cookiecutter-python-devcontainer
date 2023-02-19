from typing import Generator
import pytest
import docker
from pytest_cookies.plugin import Cookies, Result
from docker.client import DockerClient

from .utils import get_from_pyproject_toml


@pytest.fixture(scope="session")
def docker_client() -> DockerClient:
    return docker.client.from_env()


@pytest.fixture(scope="session", params=["3.8", "3.9", "3.10", "3.11"])
def baked_example_project(cookies: Cookies, request) -> Generator[Result, None, None]:
    yield cookies.bake(
        extra_context={
            "project_name": "example_project",
        }
    )


@pytest.fixture(scope="session")
def example_project_unittest_docker_image(
    docker_client: DockerClient, baked_example_project: Result
):
    pyproject_toml_file = baked_example_project.project_path / "pyproject.toml"
    project_name = get_from_pyproject_toml(pyproject_toml_file, "tool.poetry.name")
    project_version = get_from_pyproject_toml(
        pyproject_toml_file, "tool.poetry.version"
    )
    image_tag = f"{project_name}:{project_version}"
    docker_client.images.build(
        path=baked_example_project.project_path,
        dockerfile="Dockerfile",
        tag=image_tag,
        target="test",
    )
