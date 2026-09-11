from generator.util.character import Character


class SenPai(Character):
    def __init__(self, affinity: int = 0):
        super().__init__("学姐")
        self.affinity = affinity


学姐 = SenPai(0)
