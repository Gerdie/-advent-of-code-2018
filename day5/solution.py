all_chars = 'abcdefghijklmnopqrstuvwxyz'
char_list = []


def reactive(char1, char2):
    if char1 == char2:
        return False
    if char1.upper() == char2:
        return True
    if char1.lower() == char2:
        return True
    return False


with open('input.txt') as input_file:
    file_str = input_file.read()
    for char in file_str:
        if not char_list:
            char_list.append(char)
        elif reactive(char, char_list[-1]):
            char_list = char_list[:-1]
        else:
            char_list.append(char)

print('Part One: {}'.format(len(char_list)))

result_length = None

for char in all_chars:
    modified_list = []
    with open('input.txt') as input_file:
        file_str = input_file.read()
        for letter in file_str:
            if letter.lower() == char:
                continue
            modified_list.append(letter)

    result_list = []
    for letter in modified_list:
        if not result_list:
            result_list.append(letter)
        elif reactive(letter, result_list[-1]):
            result_list = result_list[:-1]
        else:
            result_list.append(letter)

    if result_length is None:
        result_length = len(result_list)
    if len(result_list) < result_length:
        result_length = len(result_list)


print('Part Two: {}'.format(result_length))
