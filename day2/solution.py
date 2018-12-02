from collections import Counter
two_count = 0
three_count = 0

with open('input.txt') as open_file:
    for line in open_file:
        counted_line = Counter(line.strip())
        if 2 in counted_line.values():
            two_count += 1
        if 3 in counted_line.values():
            three_count += 1

print('Part One: {}'.format(two_count * three_count))


def differ_by_one(str1, str2):
    diffs = 0
    diff_idx = None
    for i, char in enumerate(str1):
        if str2[i] != char:
            diffs += 1
            diff_idx = i
            if diffs > 1:
                return
    return diff_idx

strs_to_compare = set([])
with open('input.txt') as open_file:
    for line in open_file:
        line = line.strip()
        strs_to_compare.add(line)


while strs_to_compare:
    to_compare = strs_to_compare.pop()
    for other_str in strs_to_compare:
        diff_idx = differ_by_one(to_compare, other_str)
        if diff_idx is not None:
            print('Part Two: {}'.format(to_compare[:diff_idx] + to_compare[diff_idx + 1:]))
            exit()
