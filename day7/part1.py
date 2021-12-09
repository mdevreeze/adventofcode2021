def get_answer(filename):
  with open(filename, "r") as file:
    numbers = list(map(int, file.readline().replace("\n", "").split(",")))

    biggest_number = max(numbers)
    print(biggest_number)
    lowest_number = min(numbers)
    print(lowest_number)

    answers = {}
    for p in range(lowest_number, biggest_number):
        current_cost = 0
        for n in numbers:
            cost = abs(n - p)
            current_cost += cost
        answers[p] = current_cost
    
    lowest = min(answers, key=answers.get)
    return answers[lowest]
    

print("Example answer is:", get_answer("./example"))
print("Input answer is:", get_answer("./input"))