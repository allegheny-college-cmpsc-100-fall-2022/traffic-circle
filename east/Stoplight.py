import narrator

from datetime import datetime, timedelta
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    light_flag = check_flag("east_light")
    light_time = check_flag("east_turn")
    self.state = light_flag if light_flag else "🔴"
    self.timing = light_time if light_time else "00:00:00"

  def __str__(self) -> str:
    self.state += "\n➡️" if self.turn_signal else ""
    return self.state

  def __time_now(self) -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")

  def __timing(self) -> bool:
    now = datetime.strptime(self.__time_now(), "%H:%M:%S")
    then = datetime.strptime(self.timing, "%H:%M:%S")
    difference = now - then
    return (now - then).total_seconds() > 5

  def use(self) -> None:
    # Do not alter
    light = self.state
    turn = not self.__timing()
    hold = not self.timing == "00:00:00"
    # Do not alter

    #----------------------
    # TODO: Using variables light, hold, and turn, write the if statement
    #       logic to implement this Stoplight via the requirements in the README
    #
    #       Note: this uses may use the "not" prefix on either turn or hold (or
    #             both); this is like saying "the opposite of." For example:
    #             
    #       "not turn" would mean that the turn signal shouldn't be on
    #
    #       light: color of stoplight (string)
    #       turn: if turn signal should be on (boolean)
    #       hold: if the signal should hold its current state (boolean)
    #
    #       light colors as strings: 🔴 🟡 🟢
    #
    #       Note: you do not need to worry about the turn signal string, just
    #             the turn variable
    #----------------------
    
    # Do not alter
    self.state = light
    self.turn_signal = turn
    set_flag("east_light", self.state)
    if turn and self.__timing():
      set_flag("east_turn", self.__time_now())
    elif light == "🟢" and not turn: 
      set_flag("east_turn", "00:00:00")
    # Do not alter

def main():
  obj = Stoplight()
  obj.use()
  print(obj)

if __name__ == "__main__":
  main()