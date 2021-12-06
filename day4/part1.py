from itertools import chain
from types import resolve_bases

def board_win_combinations(board_array):
  combinations = []

  for x in range(5):
    x_combinations = []
    y_combinations = []
    for y in range(5):
      x_combinations.append(board_array[y][x])
      y_combinations.append(board_array[x][y])
    combinations.append(x_combinations)
    combinations.append(y_combinations)

  return combinations

def winning_combination(combination, numbers):
  for n in combination:
    if n not in numbers:
      return False
  return True

def get_winning_boards(boards, numbers):
  board_combinations = list(map(board_win_combinations, filter(len, boards))) # map boards to boards with all possible win combinations, filter out empty arrays
  
  winning_board_numbers = []
  past_numbers = []
  for n in numbers:
    if len(winning_board_numbers) > 0:
      break # we already found the winners, game is over

    past_numbers.append(n)

    for n in range(0, len(board_combinations)):
      board = boards[n]
      for combination in board:
        if winning_combination(combination, past_numbers):
          winning_board_numbers.append(n)
          break # found winning combination, do not search futher

  return { "winning_board_numbers": winning_board_numbers, "past_numbers": past_numbers }
    

def get_answer(filename):
  with open(filename, "r") as file:
    numbers = map(int, file.readline().replace("\n", "").split(","))
    boards = []
    new_board = []
    for line in file.readlines():
      if line == "\n": 
        # start new board after every empty line
        new_board = []
        boards.append(new_board)
        continue
      new_board.append(list(map(int, filter(lambda v: v != "", line.replace("\n", "").split(" "))))) # split on whitespace and filter empty values, map as ints
    
    result = get_winning_boards(boards, numbers)
    winning_board_numbers = result["winning_board_numbers"]
    past_numbers = result["past_numbers"]
    for b in winning_board_numbers:
      all_numbers_in_board = list(chain.from_iterable(boards[b]))
      all_unmarked_numbers = list(filter(lambda n: n not in past_numbers, all_numbers_in_board))
      last_number = past_numbers[-1]
      sum_numbers = sum(all_unmarked_numbers)
      return sum_numbers * last_number

print("Example answer:", get_answer("./example"))
print("Input answer:", get_answer("./input"))