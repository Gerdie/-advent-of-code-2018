initial_marker_len = len('initial state: ')
patterns = []
states = []
starting_pot_number = 0

with open('input.txt') as input_file:
    for idx, line in enumerate(input_file):
        if idx == 0:
            initial_state = line[initial_marker_len:].strip()
            states.append(initial_state)
            print("initial_state: ")
            print(initial_state)
        else:
            if line.strip():
                patterns.append(line.strip())

print("patterns: ")
print patterns

for i in xrange(20):
    last_state = states[-1]
    next_state = ''
    # add padding to each side
    last_state = '..' + last_state + '..'
    starting_pot_number -= 2
    for pot_idx, pot in enumerate(last_state):
        # don't check the padding we just added
        if pot_idx in {0, 1, len(last_state) - 2, len(last_state) - 1}:
            next_state += '.'
            continue
        added = False
        for pattn in patterns:
            if pattn[:5] == last_state[pot_idx - 2: pot_idx + 3]:
                next_state += pattn[-1]
                # print('match @ {}!'.format(pot_idx - 2 - (2 * i)))
                added = True
                break
        if not added:
            next_state += '.'
        # print(next_state)
    print("{}: {}".format(i+1, next_state))
    states.append(next_state)
    # exit()

print(states[-1])
total = 0

for pot in states[-1]:
    if pot == '#':
        print('pot in {}'.format(starting_pot_number))
        total += starting_pot_number
    starting_pot_number += 1

print(total)
# 2738 too low




