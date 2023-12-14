def get_input():
    file_path = 'inputs/example.txt'
    with open(file_path, 'r') as file:
        return file.readlines()   

def part_1():
    max_calories = 0
    current_calories = 0
    data = get_input()
    for line in data:
        if line != '\n':
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
    return  max_calories

def part_2():
    pass

if __name__ == "__main__":
    print('Part 1: ', part_1())
