from pathlib import Path
import toml
from typing import Optional


def get_from_pyproject_toml(pyproject_toml: Path, attr: str) -> Optional[str]:
    text_data = pyproject_toml.read_text("utf-8")
    data = toml.loads(text_data)
    for key in attr.split("."):
        data = data.get(key)
        if data is None:
            break
    return data
