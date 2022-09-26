import os
import sys
import shutil
import narrator

from importlib import import_module
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Car(FixtureSpec):

    def __init__(self):
        super().__init__()
        #self. n = narrator.Narrator()
        self.curr_dir = check_flag("cwd")

    def __get_light(self, direction) -> any:
        stoplight = import_module(
            f"{direction}.Stoplight"
        )
        return stoplight.Stoplight()

    def use(self, direction: str = "north") -> None:
        # Do not alter
        move_to = None
        stoplight = self.__get_light(direction)
        stoplight.use()
        signal = str(stoplight)
        # Do not alter

        #------------------------
        # TODO: Create conditional (if statement) logic to allow the 
        #       car to continue if only encountering 🟢 lights
        #
        #       The logic for the turn signal should ask what direction
        #       to turn if the car encounters "🟢\n➡️" (turn signal)
        #    
        #       Note: you must use the move_to variable to record either
        #             the input above or the direction parameter
        #     
        #       Note: Don't forget to add the input in the main()!
        #------------------------

        # Do not alter
        if move_to:
            shutil.move(
                f"{os.getcwd()}/Car.py",
                os.path.join(
                    self.curr_dir,
                    move_to
                )
            )
        # Do not alter

def main():
    #------------------------
    # TODO: Take input for where the car should go; keep in mind
    #       that the available values are north, south, east, west.
    #
    #       How does that factor into your ability to use if statements?
    #
    #       Note: you must use the identifier "direction" to keep track of this
    #             as it's used below to transmit the chosen direction to
    #             the Car.
    #------------------------

    cwd = check_flag("cwd")

    sys.path.append(cwd)

    obj = Car()
    obj.use(direction)

    # Keep track of where this thing has gone
    if os.path.exists(f"{cwd}/.car"):
        os.unlink(f"{cwd}/.car")
    os.symlink("Car.py",f"{cwd}/.car")

if __name__ == "__main__":
    main()