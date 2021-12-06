def lines_to_list(file):
  return list(map(lambda l: l.replace("\n", ""), file.readlines()))


def calculate_answer(filename):
  horizontal = 0
  depth = 0
  with open(filename, "r") as example:
    for line in lines_to_list(example):
      split = line.split(" ")
      value = int(split[1])
      action = split[0]
      if action == "forward":
        horizontal+= value
      if action == "down":
        depth+= value
      if action == "up":
        depth-= value
  return horizontal * depth

print(calculate_answer("./example"))
print(calculate_answer("./input"))