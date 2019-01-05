import re

re_patt = '(?P<x>\d+),\s(?P<y>\d+)'

counter = {'.': 0}
infinite = set([])

points = []
max_y = None
min_y = None
max_x = None
min_x = None

# Parse input and find bounds of graph
with open('input.txt') as open_file:
    for line in open_file:
        match = re.search(re_patt, line)
        x = int(match.group('x'))
        y = int(match.group('y'))
        if not max_x or x > max_x:
            max_x = x
        if not min_x or x < min_x:
            min_x = x
        if not max_y or y > max_y:
            max_y = y
        if not min_y or y < min_y:
            min_y = y

        points.append((x, y))

# Create empty bounded graph
graph = [['-' for x in xrange(max_x + 1)] for y in xrange(max_y + 1)]

# Set points on graph
for idx, pt in enumerate(points):
    x, y = pt
    graph[y][x] = idx
    counter[idx] = 1


# For debugging
def print_graph():
    for row in graph:
        print(row)


# Not fast, not dry
def find_closest_manhattan(x, y):
    going_right = [(x + 1, y)]
    going_left = [(x - 1, y)]
    going_up = [(x, y + 1)]
    going_down = [(x, y - 1)]
    found_letters = []

    while True:
        if going_right:
            next_rights = []
            for pt in going_right:
                x_pos, y_pos = pt
                if x_pos <= max_x:
                    pt_value = graph[y_pos][x_pos]
                    if pt_value != '-':
                        found_letters.append(pt_value)
                    next_rights.append((x_pos + 1, y_pos))
            going_right = next_rights
        if going_left:
            next_lefts = []
            for pt in going_left:
                x_pos, y_pos = pt
                if x_pos >= 0:
                    pt_value = graph[y_pos][x_pos]
                    if pt_value != '-':
                        found_letters.append(pt_value)
                    next_lefts.append((x_pos - 1, y_pos))
            going_left = next_lefts
        if going_up:
            next_ups = []
            for pt in going_up:
                x_pos, y_pos = pt
                if y_pos <= max_y:
                    pt_value = graph[y_pos][x_pos]
                    if pt_value != '-':
                        found_letters.append(pt_value)
                    next_ups.append((x_pos, y_pos + 1))
                    going_right.append((x_pos + 1, y_pos))
                    going_left.append((x_pos - 1, y_pos))
            going_up = next_ups
        if going_down:
            next_downs = []
            for pt in going_down:
                x_pos, y_pos = pt
                if y_pos >= 0:
                    pt_value = graph[y_pos][x_pos]
                    if pt_value != '-':
                        found_letters.append(pt_value)
                    next_downs.append((x_pos, y_pos - 1))
                    going_right.append((x_pos + 1, y_pos))
                    going_left.append((x_pos - 1, y_pos))
            going_down = next_downs

        if found_letters:
            break

    if len(found_letters) == 1:
        return found_letters[0]
    if len(found_letters) > 1:
        return '.'


for y, row in enumerate(graph):
    for x, pt in enumerate(row):
        if graph[y][x] != '-':
            continue
        closest = find_closest_manhattan(x, y)
        counter[closest] += 1

        if y == 0 or y == max_y:
            infinite.add(closest)
        if x == 0 or x == max_x:
            infinite.add(closest)
    if y % 10 == 0:
        print('finished row {}'.format(y))


non_infinite_max = max([counter[letter] for letter in counter if letter not in infinite])
print('Part One: {}'.format(non_infinite_max))
