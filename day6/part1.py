class LaternFish:
  def __init__(self, internal_timer):
    self.internal_timer = internal_timer

  def day_older(self, on_new_fish):
    if not self.check_new_fish(on_new_fish):
      self.internal_timer -= 1

  def check_new_fish(self, on_new_fish):
    if self.internal_timer != 0:
      return False
    self.internal_timer = 6
    on_new_fish(LaternFish(8))
    return True
  
  def __str__(self) -> str:
    return str(self.internal_timer)


fishes = []

def on_new_fish(fish):
  fishes.append(fish)

def get_answer(filename):
  with open(filename, "r") as file:
    numbers = list(map(int, file.readline().replace("\n", "").split(",")))
    for n in numbers: 
      fishes.append(LaternFish(n))

    for day in range(0, 80):
      len_fishes = len(fishes)
      for i in range(0, len_fishes):
        fish = fishes[i]
        fish.day_older(on_new_fish)
      print("After day ", day, list(map(str,fishes)))
    return len(fishes)

print("Example answer is:", get_answer("./example"))
print("Input answer is:", get_answer("./input"))