import re

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
re_patt = '(?P<x>\d+),\s(?P<y>\d+)'

points = []
max_y = None
min_y = None
max_x = None
min_x = None

with open('test_input.txt') as open_file:
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

graph = [['-' for x in xrange(max_x + 1)] for y in xrange(max_y + 1)]


def print_graph():
    for row in graph:
        print(row)


for idx, pt in enumerate(points):
    print(pt)
    x, y = pt
    graph[y][x] = alpha[idx]

print_graph()
