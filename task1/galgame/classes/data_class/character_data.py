from dataclasses import dataclass


@dataclass
class CharacterData:
    id: str = "none"
    name: str = "none"


@dataclass
class JieJieData(CharacterData):
    id: str = "jie_jie"
    name: str = "姐姐"
    affinity: int = 0


@dataclass
class SenPaiData(CharacterData):
    id: str = "sen_pai"
    name: str = "学姐"
    affinity: int = 0


@dataclass
class XiaoBaiData(CharacterData):
    id: str = "xiao_bai"
    name: str = "小白"
    affinity: int = 0
