from enum import Enum
from pathlib import Path
from typing import Any


# Pylance我错了喵，泥不要在用类型不确定肘击我了
def to_dict(obj: Any) -> Any:
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]  # type: ignore
    elif isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}  # type: ignore
    elif hasattr(obj, "__dict__"):
        result: dict[str, Any] = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, list):
                result[key] = [to_dict(item) for item in value]  # type: ignore
            elif isinstance(value, dict):
                result[key] = {k: to_dict(v) for k, v in value.items()}  # type: ignore
            elif isinstance(value, Enum):
                result[key] = value.value
            elif hasattr(value, "__dict__"):
                result[key] = to_dict(value)
            else:
                result[key] = value
        return result
    else:
        return obj


def get_galgame_path():
    current = Path(__file__).resolve()
    for parent in current.parents:
        if parent.name == "galgame":
            path = parent
            break
    else:
        path = Path("galgame")

    return path
