# Cookiecutter Python Dev Container

Modern Python dev environment inside Docker container.
## Quickstart
Install `cookiecutter` tool if you don't have one already installed and run following command.
```shell
cookiecutter https://github.com/audreyfeldroy/cookiecutter-python-devcontainer.git
```
Cookiecutter installation instructions of official [wiki](https://cookiecutter.readthedocs.io/en/stable/installation.html).

## Features
Dev environment inside container pre-installed with:

* [`poetry`](https://python-poetry.org/) for managing project dependencies
* Predefined VS Code extensions (list of default VS Code extensions is available in `.devcontainer/devcontainer.json`)
* [mypy](https://mypy.readthedocs.io/en/stable/) 
* [pytest](https://docs.pytest.org/en/7.1.x/)
* [black](https://github.com/psf/black)
* [coverage](https://coverage.readthedocs.io/en/6.4.2/)
* [isort](https://pypi.org/project/isort/)
* [flake8](https://flake8.pycqa.org/en/latest/)



