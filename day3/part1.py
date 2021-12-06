def lines_to_list(file):
  return list(map(lambda l: l.replace("\n", ""), file.readlines()))

def calculate_answer(filename):
  with open(filename, "r") as example:
    indexed_chars = []
    for line in lines_to_list(example):
      i = 0
      for char in line:
        if i + 1 > len(indexed_chars):
          indexed_chars.append([])
        indexed_chars[i].append(char)
        i+=1
    
    max_output = ""
    min_output = ""
    for index in indexed_chars:
      max_output += str(max(set(index), key = index.count)) # get most occuring value in array
      min_output += str(min(set(index), key = index.count)) # least
    return int(max_output, 2) * int(min_output, 2)


print(calculate_answer("./example"))
print(calculate_answer("./input"))