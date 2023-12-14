# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that 
# the Elves now need to recover. On each line, the calibration value 
# can be found by combining the first digit and the last digit 
# (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 
#12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. 
# What is the sum of all of the calibration values?



from fnmatch import translate


def get_input():
    file_path = 'inputs/input_day01.txt'
    with open(file_path, 'r') as file:
        return file.readlines()   

def part_1():
    data = get_input()
    results=[]
    for line in data:
        if line:
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)

             # Combine the digits to form a two-digit number
            if first_digit is not None and last_digit is not None:
                calibration_value = int(first_digit + last_digit)
                results.append(calibration_value)

    print('part1:' , sum(results))



# Your calculation isn't quite right. It looks like some of the digits are actually 
# spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
# also count as valid "digits".
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# Equipped with this new information, you now need to find the real first and last 
# digit on each line. For example:


# In this example, the calibration values are 
# 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?
def part_2():
    data = get_input()
    word_to_number = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    results = []
    
    for line in data:
        matched_numbers = []
        for item in word_to_number:
            indices = [i for i in range(len(line)) if line.startswith(item, i) or line.startswith(word_to_number[item], i)]
            for index in indices:
                matched_numbers.append((item, word_to_number[item], index))

        if matched_numbers:
            sorted_numbers = [word_to_number[word] for word, _, _ in sorted(matched_numbers, key=lambda x: x[2])]
            calc = int(sorted_numbers[0] + sorted_numbers[-1])
            results.append(calc)


    print('part2:', sum(results))

if __name__ == "__main__":
    part_1()
    part_2() #55902
