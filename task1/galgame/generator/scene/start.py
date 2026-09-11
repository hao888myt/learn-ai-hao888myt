from character.jiejie import 姐姐
from character.me import 我
from generator.util.dialogue_util import (
    Choice,
    ChoiceGroup,
    DialogueExporter,
    DialogueGroup,
    Effect,
    EffectType,
    Narration,
)


def generator():
    DialogueExporter(
        "start",
        [
            DialogueGroup(
                "group_1",
                [
                    Narration("你是一名刚刚踏入大学校园的新生。"),
                    Narration(
                        "在开学典礼上，拿下压倒性成绩第一的你被选为新生代表发言。"
                    ),
                    Narration(
                        "在全场上千人的注视下，你气质非凡，发言流畅，很快成为焦点人物。"
                    ),
                    Narration("消息迅速传开，关于‘神秘新生代表’的讨论充斥着整个校园。"),
                    Narration("于是，在这个新的舞台上，你与三位不同的女生产生了交集……"),
                ],
                "group_2",
            ),
            ChoiceGroup(
                "group_2",
                "你的选择是？",
                [
                    Choice("jiejie", "sds", "group_1"),
                    Choice("jiejie", "sds", "group_1"),
                    Choice("jiejie", "sds", "group_1").add_effect(
                        Effect(EffectType.MODIFY_AFFINITY, 1)
                    ),
                ],
            ),
        ],
    )
