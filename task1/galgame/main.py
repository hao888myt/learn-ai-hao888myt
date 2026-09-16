import importlib
import inspect
import json
from pathlib import Path
from typing import Any

from classes.data_class.save_data import SaveData
from classes.loader.file_loader import FileLoader
from classes.util.util import get_galgame_path, to_dict

SAVE_PATH = Path("data/save")


def run_all_generators():
    for file in Path("scene").glob("*.py"):
        if file.name.startswith("__"):
            continue
        name = file.stem
        module = importlib.import_module(f"scene.{name}")
        if hasattr(module, "generator"):
            module.generator()
        else:
            print(f"{name}.py没有generator()函数")


def instantiate_all() -> dict[str, Any]:
    """实例化character文件夹的所有类"""
    folder: str = "classes/data_class"
    results: dict[str, Any] = {}

    py_file = Path(f"{folder}/character_data.py")

    module_name = py_file.stem

    # 动态导入
    module = importlib.import_module(f"{folder.replace("/", ".")}.{module_name}")

    # 找模块里的类
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # 只处理本模块定义的类（排除导入的类）
        if obj.__module__ == module.__name__ and name != "CharacterData":
            instance = obj()

            character_dict = to_dict(instance)
            character_dict.pop("id", None)

            results[instance.id] = character_dict  # type: ignore
            print(f"已实例化 {module_name}.{name}")

    return {"characters": to_dict(results), "save": to_dict(SaveData())}


def create_new_game():
    output_path = get_galgame_path() / SAVE_PATH / "data.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(instantiate_all(), f, ensure_ascii=False, indent=2)


def load_game():
    file = FileLoader(SAVE_PATH, "data").get_json()

    characters = file.get("characters")
    if isinstance(characters, list):
        for character in characters:  # type: ignore
            if isinstance(character, dict) and character.get("name") == "我":  # type: ignore
                print(character)  # type: ignore


def save_game():
    pass


if __name__ == "__main__":
    run_all_generators()

    folder = SAVE_PATH
    if not any(folder.iterdir()):
        print("没有玩家存档，正在创建中")
        create_new_game()

    # load_game()
