from operator import index
import re


def get_input():
    file_path = 'inputs/input_day02.txt'
    with open(file_path, 'r') as file:
        return file.readlines()   


# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# Determine which games would have been possible 
# if the bag had been loaded with only 
# 12 red cubes, 
# 13 green cubes, 
# and 14 blue cubes. 
# What is the sum of the IDs of those games?

# Game 1,2 and 5 would be possible

def part_1():
    data = get_input()
    existing_color_counts = {
        'blue': 14,
        'green': 13,
        'red': 12
    }
    add_index = []   
    remove_index = []

    for line in data:

        game_number_match = re.search(r'Game (\d+):', line)
        index = int(game_number_match.group(1))
        subsets = line.split(';')

        for subset in subsets:

            matches = re.findall(r'(\d+) (\w+)', subset)  
            color_counts = {'blue': 0, 'green': 0, 'red': 0}
            for count, color in matches:
                color_counts[color] = int(count)

            all_less_than_or_equal = all(color_counts[color] <= existing_color_counts[color] for color in color_counts)
            add_index.append(index)
            if not all_less_than_or_equal:
                remove_index.append(index)
    add = set(add_index)
    remove = set(remove_index)
    result = sum(add) - sum(remove)   
        
    return result


# Part 2
# in each game you played, what is the fewest number of cubes 
# of each color that could have been in the bag to make the game possible?

def part_2():
    data = get_input()
    blue_value = []
    red_value = []
    green_value = []
    line_value = []
    for line in data:
        subsets = line.split(';')
        color_counts = {'blue': 0, 'green': 0, 'red': 0}

        for subset in subsets:
            matches = re.findall(r'(\d+) (\w+)', subset)
            for count, color in matches:
                color_counts[color] = max(color_counts[color], int(count))

        blue_value.append(color_counts['blue'])
        red_value.append(color_counts['red'])
        green_value.append(color_counts['green'])

        highest_blue = blue_value[-1]
        highest_red = red_value[-1]
        highest_green = green_value[-1]
        values = highest_blue * highest_green * highest_red
        line_value.append(values)

    return (sum(line_value))    

if __name__ == "__main__":
    print('Part 1 ', part_1())
    print('Part 2 ', part_2())
