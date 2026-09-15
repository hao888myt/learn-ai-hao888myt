from ..util.dialogue_helper import Dialogue


class Character:
    def __init__(self, name: str):
        self.name = name

    def talk(self, content: str) -> Dialogue:
        return Dialogue(self.name, content)
