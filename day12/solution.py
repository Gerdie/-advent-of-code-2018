initial_marker_len = len('initial state: ')
patterns = set()
starting_pot_number = 0

with open('input.txt') as input_file:
    for idx, line in enumerate(input_file):
        if idx == 0:
            initial_state = line[initial_marker_len:].strip()
            last_state = list(initial_state)
        else:
            line = line.strip()
            if line and line.endswith('#'):
                patterns.add(line[:5])

for i in xrange(20):
    next_state = []
    # add padding to each side
    if not last_state[:3] == ['.', '.', '.']:
        last_state = ['.', '.', '.'] + last_state
        starting_pot_number -= 3
    if not last_state[-3:] == ['.', '.', '.']:
        last_state.extend(['.', '.', '.'])

    for pot_idx, pot in enumerate(last_state):
        # don't check the padding we just added
        if pot_idx in {0, 1, len(last_state) - 2, len(last_state) - 1}:
            next_state.append('.')
            continue

        if ''.join(last_state[pot_idx - 2: pot_idx + 3]) in patterns:
            next_state.append('#')
        else:
            next_state.append('.')

    last_state = next_state
    # print progress
    if i % 1000 == 0:
        print('Iteration {}'.format(i))

total = 0
for pot in last_state:
    if pot == '#':
        total += starting_pot_number
    starting_pot_number += 1

# Part One: 2823
print('Part Two: {}'.format(total))




