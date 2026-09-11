import json
from enum import Enum
from pathlib import Path
from typing import Any


class Dialogue:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content


class Narration(Dialogue):
    def __init__(self, content: str):
        self.name = ""
        self.content = content


class ConditionType(Enum):
    REQUIRED_AFFINITY = "required_affinity"


class Condition:
    def __init__(self, type: ConditionType, value: Any) -> None:
        self.type = type
        self.value = value


class EffectType(Enum):
    MODIFY_AFFINITY = "modify_affinity"


class Effect:
    def __init__(self, type: EffectType, value: Any) -> None:
        self.type = type
        self.value = value


class Choice:
    def __init__(self, character: str, content: str, group_to: str):
        self.character = character
        self.content = content
        self.group_to = group_to
        self.effects: list[Effect] = []
        self.conditions: list[Condition] = []

    def add_condition(self, condition: Condition | list[Condition]):
        if isinstance(condition, Condition):
            self.conditions.append(condition)
        else:
            self.conditions.extend(condition)

        return self

    def add_effect(self, effect: Effect | list[Effect]):
        if isinstance(effect, Effect):
            self.effects.append(effect)
        else:
            self.effects.extend(effect)

        return self


class DialogueGroup:
    def __init__(self, id: str, dialogues: list[Dialogue], group_to: str):
        self.type = "dialogue_group"
        self.id = id
        self.dialogues = dialogues
        self.group_to = group_to


class ChoiceGroup:
    def __init__(self, id: str, desc: str, choices: list[Choice]):
        self.type = "choice_group"
        self.id = id
        self.desc = desc
        self.choices = choices


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


class DialogueExporter:
    def __init__(
        self,
        file_name: str,
        groups: list[DialogueGroup | ChoiceGroup],
    ):
        output_dir: Path

        # 判断galgame/data文件夹在哪
        current = Path(__file__).resolve()
        for parent in current.parents:
            if parent.name == "galgame":
                output_dir = parent / "data"
                break
        else:
            output_dir = Path("galgame/data")

        output_path = Path(output_dir) / f"{file_name}.json"

        # 一键创建目录
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # 数据导出
        data = to_dict({"groups": groups})

        # 生成json文件
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"已生成 {file_name}.json 于 {output_path}")
