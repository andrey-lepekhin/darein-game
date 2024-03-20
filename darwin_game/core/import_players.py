import importlib
import inspect
import os

from darwin_game.models.player import Player


def find_import_player_classes(directory: str, exclude_dirs: list[str] = []) -> list[type[Player]]:
    player_classes = []

    for root, dirs, files in os.walk(directory):
        if root.split("/")[-1] in exclude_dirs:
            continue
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # Convert file path to a module path
                module_path = os.path.join(root, file).replace("/", ".").replace("\\", ".")
                module_path = module_path[:-3]  # Remove '.py' extension

                # Dynamically import the module
                module = importlib.import_module(module_path)

                # Inspect the module for classes that are subclasses of Player
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Player) and obj is not Player:
                        player_classes.append(obj)

    return player_classes  # type: ignore
