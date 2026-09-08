import json
from enum import Enum
from typing import Any, List, Union, cast


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
        self.id = id
        self.dialogues = dialogues
        self.group_to = group_to


class ChoiceGroup:
    def __init__(self, id: str, desc: str, choices: list[Choice]):
        self.id = id
        self.desc = desc
        self.choices = choices


def to_dict(obj: Any) -> Any:
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]  # type: ignore
    elif isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}
    elif hasattr(obj, "__dict__"):
        result: dict[str, Any] = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, list):
                result[key] = [to_dict(item) for item in value]
            elif isinstance(value, dict):
                result[key] = {k: to_dict(v) for k, v in value.items()}
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
        data: dict[str, list[dict[str, Any]]] = {"groups": []}

        for group in groups:
            if isinstance(group, DialogueGroup):
                group_dict: dict[str, Any] = {
                    "id": group.id,
                    "dialogues": [],
                    "group_to": group.group_to,
                }

                for dialogue in group.dialogues:
                    group_dict["dialogues"].append(
                        {
                            "type": "dialogue",
                            "name": dialogue.name,
                            "content": dialogue.content,
                        }
                    )

                data["groups"].append(group_dict)

            else:
                group_dict: dict[str, Any] = {
                    "id": group.id,
                    "desc": group.desc,
                    "choices": [],
                }

                for choice in group.choices:
                    group_dict["choices"].append(
                        {
                            "type": "choice",
                            "character": choice.character,
                            "content": choice.content,
                            "group_to": choice.group_to,
                            "affinity": choice.effects,
                        }
                    )

                data["groups"].append(group_dict)

        with open("dialogues.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("已生成 dialogues.json")
