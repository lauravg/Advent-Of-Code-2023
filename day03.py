import re


def get_input():
    file_path = 'inputs/input_day03.txt'
    with open(file_path, 'r') as file:
        return file.readlines()


def part_1():
    data = get_input()
    sum_of_part_numbers = 0

    for index, line in enumerate(data):
        symbols_matches = re.finditer(r'[^\w\s.]', line)
        for symbol_match in symbols_matches:
            symbol_position = symbol_match.start()

            if index - 1 >= 0:
                for number_match_prev in re.finditer(r'\d+', data[index - 1]):
                    start, end = number_match_prev.span()
                    if start - 1 <= symbol_position <= end:
                        sum_of_part_numbers += int(number_match_prev.group())

            if index + 1 < len(data):
                for number_match_next in re.finditer(r'\d+', data[index + 1]):
                    start, end = number_match_next.span()
                    if start - 1 <= symbol_position <= end:
                        sum_of_part_numbers += int(number_match_next.group())

            for number_match_same in re.finditer(r'\d+', line):
                start, end = number_match_same.span()
                if start - 1 <= symbol_position <= end:
                    sum_of_part_numbers += int(number_match_same.group())

    return sum_of_part_numbers


def part_2():
    data = get_input()
    part_result = 0
    result = 0
    for index, line in enumerate(data):
        star_symbols_matches = re.finditer(r'[*]', line)
        for symbol_match in star_symbols_matches:
            symbol_position = symbol_match.start()
            if symbol_match.group():

                same_line_values = []
                for number_match_same in re.finditer(r'\d+', line):
                    start, end = number_match_same.span()
                    if symbol_position == start - 1 or symbol_position == end:
                        same_line_values.append(int(number_match_same.group()))

                prev_line_values = []
                if index >= 1:
                    for number_match_prev in re.finditer(r'\d+', data[index - 1]):
                        start, end = number_match_prev.span()
                        if start - 1 <= symbol_position <= end:
                            prev_line_values.append(
                                int(number_match_prev.group()))

                next_line_values = []
                if index + 1 < len(data):
                    for number_match_next in re.finditer(r'\d+', data[index + 1]):
                        start, end = number_match_next.span()
                        if start - 1 <= symbol_position <= end:
                            next_line_values.append(
                                int(number_match_next.group()))

                # print('test', next_line_values)
                if (
                    len(same_line_values) >= 2
                    and same_line_values[0] != None
                    and same_line_values[1] != None
                ):
                    part_result = same_line_values[0] * same_line_values[1]
                    result += part_result

                elif (
                    len(prev_line_values) >= 2
                    and prev_line_values[0] != None
                    and prev_line_values[1] != None
                ):
                    part_result = prev_line_values[0] * prev_line_values[1]
                    result += part_result

                elif (
                    len(next_line_values) >= 2
                    and next_line_values[0] != None
                    and next_line_values[1] != None
                ):
                    part_result = next_line_values[0] * next_line_values[1]
                    result += part_result

                elif (
                    len(same_line_values) >= 1 and len(next_line_values) >= 1

                ):
                    part_result = same_line_values[0] * next_line_values[0]
                    result += part_result

                elif (
                    len(same_line_values) >= 1 and len(prev_line_values) >= 1

                ):
                    part_result = same_line_values[0] * prev_line_values[0]
                    result += part_result

                elif (
                    len(prev_line_values) >= 1 and len(next_line_values) >= 1
                ):
                    part_result = prev_line_values[0] * next_line_values[0]
                    result += part_result

    return result


if __name__ == "__main__":
    print('Part 1: ', part_1())  # 539590
    print('Part 2:', part_2())  # 80703636