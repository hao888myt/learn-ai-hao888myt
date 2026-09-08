from util.dialogue_util import (
    Choice,
    ChoiceGroup,
    Dialogue,
    DialogueGroup,
    GroupManager,
)

GroupManager(
    [
        DialogueGroup(
            "group_1",
            [
                Dialogue("asd", "你好你好"),
                Dialogue("dsa", "你好你好"),
                Dialogue("asd", "同学再见"),
                Dialogue("dsa", "同学再见"),
            ],
            "",
        ),
        ChoiceGroup(
            "group_2",
            "你好",
            [
                Choice("老大", "sds", "group_1"),
                Choice("老大", "sds", "group_1"),
                Choice("老大", "sds", "group_1"),
            ],
        ),
    ]
)
