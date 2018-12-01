frequency = 0
frequency_set = set([frequency])

with open('input.txt') as input_file:
    for line in input_file:
        symbol = line[0]
        quantity = int(line[1:])
        if symbol == '+':
            frequency += quantity
        elif symbol == '-':
            frequency -= quantity

print('Part One: {}'.format(frequency))


def loop_through_file(frequency=0):
    with open('input.txt') as input_file:
        for line in input_file:
            symbol = line[0]
            quantity = int(line[1:])
            if symbol == '+':
                frequency += quantity
            elif symbol == '-':
                frequency -= quantity
            if frequency in frequency_set:
                return frequency
            else:
                frequency_set.add(frequency)
    return loop_through_file(frequency=frequency)

print('Part Two: {}'.format(loop_through_file(frequency=0)))
