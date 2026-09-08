class Character:
    def __init__(self, name: str, affinity: int = 0):
        self.name = name
        self.affinity = affinity

    def modify_affinity(self, value: int) -> None:
        self.affinity += value

    def set_affinity(self, value: int) -> None:
        self.affinity = value
