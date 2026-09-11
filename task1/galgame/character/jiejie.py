from generator.util.character import Character


class JieJie(Character):
    def __init__(self, affinity: int = 0):
        super().__init__("姐姐")
        self.affinity = affinity


姐姐 = JieJie(0)
