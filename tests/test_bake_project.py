import pytest
from pytest_cookies.plugin import Cookies

from .utils import get_from_pyproject_toml


def test_bake_with_specified_python_version(cookies: Cookies):
    result = cookies.bake(extra_context={"python_version": "3.9"})
    assert result.exit_code == 0
    pyproject_toml = result.project / "pyproject.toml"
    python_version = get_from_pyproject_toml(
        pyproject_toml, "tool.poetry.dependencies.python"
    )
    assert python_version == "^3.9"


def test_bake_with_specified_project_version(cookies: Cookies):
    result = cookies.bake(extra_context={"version": "1.0.0"})
    assert result.exit_code == 0
    pyproject_toml = result.project / "pyproject.toml"
    project_version = get_from_pyproject_toml(pyproject_toml, "tool.poetry.version")
    assert project_version == "1.0.0"


def test_bake_with_specified_project_name(cookies: Cookies):
    project_name = "Project Blue Book"
    result = cookies.bake(extra_context={"project_name": project_name})
    assert result.exit_code == 0
    pyproject_toml = result.project / "pyproject.toml"
    project_name = get_from_pyproject_toml(pyproject_toml, "tool.poetry.name")
    assert project_name == "project_blue_book"
    project_package = result.project / "project_blue_book"
    assert project_package.isdir()


def test_sample_tests(cookies: Cookies):
    """
    Testing if sample unittest are finishing without errors.
    """
    result = cookies.bake(extra_context={"project_name": "sample_project"})
    tests_dir = result.project / "tests"
    exit_code = pytest.main(["-x", str(tests_dir)])
    assert exit_code == 0
