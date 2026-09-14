import importlib
import inspect
import json
from pathlib import Path
from typing import Any

from generator.util.util import to_dict


def run_all_generators():
    for f in Path("generator/scene").glob("*.py"):
        if f.name.startswith("__"):
            continue
        name = f.stem
        module = importlib.import_module(f"generator.scene.{name}")
        if hasattr(module, "generator"):
            module.generator()
        else:
            print(f"{name}.py没有generator()函数")


def instantiate_all() -> list[Any]:
    """实例化character文件夹的所有类"""
    folder: str = "character"
    results: list[Any] = []

    for py_file in Path(folder).glob("*.py"):
        if py_file.name.startswith("__"):
            continue

        module_name = py_file.stem

        # 动态导入
        module = importlib.import_module(f"{folder}.{module_name}")

        # 找模块里的类
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # 只处理本模块定义的类（排除导入的类）
            if obj.__module__ == module.__name__:
                instance = obj()
                results.append(instance)  # type: ignore
                print(f"已实例化 {module_name}.{name}")

    return to_dict(results)

if __name__ == "__main__":
    run_all_generators()
