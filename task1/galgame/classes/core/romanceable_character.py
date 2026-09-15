from classes.core.character import Character


class RomanceableCharacter(Character):
    def __init__(self, name: str, affinity: int = 0):
        super().__init__(name)
        self.affinity = affinity
