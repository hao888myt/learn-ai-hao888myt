from generator.util.character import Character


class Me(Character):
    def __init__(self):
        super().__init__("我")
        self.current_file = "start"
        self.current_group = "group_1"
        self.current_index = 0


我 = Me()
