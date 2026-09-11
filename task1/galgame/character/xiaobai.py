from generator.util.character import Character


class XiaoBai(Character):
    def __init__(self, affinity: int = 0):
        super().__init__("小白")
        self.affinity = affinity


小白 = XiaoBai(0)
