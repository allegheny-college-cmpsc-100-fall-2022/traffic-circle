import os
import sys
import random
import shutil
import narrator

from importlib import import_module
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Bus(FixtureSpec):

    def __init__(self):
        super().__init__()

    @staticmethod
    def __get_light(direction) -> str:
        stoplight = import_module(
            f"{direction}.Stoplight"
        )
        light = stoplight.Stoplight()
        light.use()
        return str(light)
    
    @staticmethod
    def __get_road() -> str:
        return os.getcwd()
    
    @staticmethod
    def __get_direction() -> str:
        road = Bus.__get_road()
        while road == Bus.__get_road():
            road = random.choice(
                ["north", "south", "east", "west"]
            )
        return road
    
    @staticmethod
    def __report(direction, stoplight) -> None:
        print(f"🚌 {direction}:\t{stoplight}")
    
    @staticmethod
    def __move_bus(direction) -> None:
        cwd = check_flag("cwd")
        if not os.path.exists(f"{cwd}/{direction}/Bus.py"):
            shutil.move(
                f"{Bus.__get_road()}/Bus.py",
                f"{cwd}/{direction}"
            )
            os.chdir(
                f"{cwd}/{direction}"
            )

    def use(self) -> None:
        direction = Bus.__get_direction()
        stoplight = Bus.__get_light(direction)
        Bus.__report(direction, stoplight)

        #------------------------
        while stoplight != "🔴":
            Bus.__move_bus(direction)
            direction = Bus.__get_direction()
            stoplight = Bus.__get_light(direction)
            Bus.__report(direction, stoplight)
        #------------------------

def main():
    # Get the current directory, add access for stoplights
    cwd = check_flag("cwd")
    sys.path.append(cwd)

    # Create the Bus so that we can use it
    obj = Bus()
    obj.use()

    # Keep track of where this thing has gone
    if os.path.exists(f"{cwd}/.bus"):
        os.unlink(f"{cwd}/.bus")
    os.symlink("Bus.py",f"{cwd}/.bus")

if __name__ == "__main__":
    main()