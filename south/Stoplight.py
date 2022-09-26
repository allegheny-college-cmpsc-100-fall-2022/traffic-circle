import narrator

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    flag = check_flag("south_light")
    self.state = flag if flag == "" else "🔴"

  def __str__(self) -> str:
    return f"{self.state}"

  def use(self) -> None:
    # Do not alter
    light = self.state
    # Do not alter

    #----------------------
    if light == "🔴":
      light = "⚫"
    elif light == "⚫":
      light = "🔴"
    #----------------------
    
    # Do not alter
    self.state = light
    set_flag("south_light", self.state)
    # Do not alter

def main():
  obj = Stoplight()
  obj.use()
  print(obj)

if __name__ == "__main__":
  main()