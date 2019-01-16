import re

re_patt = 'Step (?P<first_step>\D) must be finished before step (?P<second_step>\D) can begin.'
letters_seen = set()
steps = []


def get_step(value):
    for step in steps:
        if step.val == value:
            return step


class Step(object):
    def __init__(self, val):
        self.val = val
        self.parents = set()


with open('input.txt') as input_file:
    for line in input_file:
        match = re.search(re_patt, line)
        first_letter = match.group('first_step')
        second_letter = match.group('second_step')

        if first_letter in letters_seen:
            first_step = get_step(first_letter)
        else:
            first_step = Step(first_letter)
            steps.append(first_step)

        if second_letter in letters_seen:
            second_step = get_step(second_letter)
        else:
            second_step = Step(second_letter)
            steps.append(second_step)

        second_step.parents.add(first_letter)

        letters_seen.add(first_letter)
        letters_seen.add(second_letter)

letter_order = []
while steps:
    have_parents = []
    orphans = []
    for st in steps:
        if st.parents - set(letter_order):
            have_parents.append(st)
        else:
            orphans.append(st)
    orphans.sort(key=lambda o: o.val)

    letter_order.append(orphans[0].val)
    have_parents.extend(orphans[1:])
    steps = have_parents

print('Part One: {}'.format(''.join(letter_order)))
