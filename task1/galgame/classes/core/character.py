from ..util.dialogue_helper import Dialogue


class Character:
    name: str = "none"

    @classmethod
    def talk(cls, content: str) -> Dialogue:
        return Dialogue(cls.name, content)
