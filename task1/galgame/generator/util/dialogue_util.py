import json
from enum import Enum
from typing import Any


class Dialogue:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content


class ConditionType(Enum):
    REQUIRED_AFFINITY = "required_affinity"


class Condition:
    def __init__(self, condition_type: ConditionType, value: Any) -> None:
        self.condition_type = condition_type
        self.value = value


class EffectType(Enum):
    MODIFY_AFFINITY = "modify_affinity"


class Effect:
    def __init__(self, effect_type: EffectType, value: Any) -> None:
        self.effect_type = effect_type
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


class GroupManager:
    def __init__(self, groups: list[DialogueGroup | ChoiceGroup]):
        data = to_dict({"groups": groups})

        with open("dialogues.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("已生成 dialogues.json")
