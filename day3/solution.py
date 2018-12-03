import re
re_patt = '#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)'

claims = []
grid = [[]]


def expand_grid_to(new_x, new_y):
    for y in grid:
        y.extend([0] * (new_x - len(y)))
    for y in range(new_y - len(grid)):
        grid.append([0] * new_x)


def mark_grid(left_offset, top_offset, width, height):
    for x in range(left_offset + width):
        if x < left_offset:
            continue
        for y in range(top_offset + height):
            if y < top_offset:
                continue
            grid[y][x] += 1


def print_grid():
    for row in grid:
        print(row)


def count_doubles():
    doubles = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                doubles += 1
    return doubles

# Part One: Create Grid
with open('input.txt') as open_file:
    for line in open_file:
        line = line.strip()
        match = re.search(re_patt, line)
        claim, left_offset, top_offset, width, height = map(int, match.groups())
        claims.append((claim, left_offset, top_offset, width, height))

        if len(grid) < top_offset + height or len(grid[0]) < left_offset + width:
            expand_grid_to(left_offset + width, top_offset + height)
        mark_grid(left_offset, top_offset, width, height)

print('Part One: {}'.format(count_doubles()))


def claim_overlaps(claim, left_offset, top_offset, width, height):
    for x in range(left_offset + width):
        if x < left_offset:
            continue
        for y in range(top_offset + height):
            if y < top_offset:
                continue
            if grid[y][x] != 1:
                return True
    return False


# Part Two: Find claim without overlap
for claim_tuple in claims:
    claim, left_offset, top_offset, width, height = claim_tuple
    if not claim_overlaps(claim, left_offset, top_offset, width, height):
        part_two = claim
        break

print('Part Two: {}'.format(part_two))
