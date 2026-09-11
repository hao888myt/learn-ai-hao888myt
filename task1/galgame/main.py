import importlib
from pathlib import Path


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


if __name__ == "__main__":
    run_all_generators()
