import narrator

from datetime import datetime, timedelta
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    light_flag = check_flag("west_light")
    light_time = check_flag("west_time")
    self.state = light_flag if light_flag else "🔴"
    self.timing = light_time if light_time else "00:00:00"

  def __str__(self) -> str:
    return f"{self.state}"

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
    timeout = self.__timing()
    # Do not alter

    #----------------------
    if light == "🟡":
      light = "🔴"
    if light == "🟢" and timeout:
      light = "🟡"
    if light == "🔴" and timeout:
      light = "🟢"
    #----------------------
    
    # Do not alter
    self.state = light
    set_flag("west_light", self.state)
    if self.__timing():
      set_flag("west_time", self.__time_now())

    # Do not alter

def main():
  obj = Stoplight()
  obj.use()
  print(obj)

if __name__ == "__main__":
  main()