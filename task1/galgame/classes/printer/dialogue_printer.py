from typing import Any


class DialoguePrinter:
    def __init__(self, group: dict[str, Any], index: int = 0) -> None:
        match group.type:
            case "dialogue_group":
                pass
            case _:
                pass
