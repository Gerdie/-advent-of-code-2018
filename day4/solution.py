import re

re_patt = '(\[\d{4}-\d{2}-\d{2}\s(?P<hour>\d{2}):(?P<minute>\d{2})\])\s((Guard\s#(?P<guard_id>\d+)\sbegins\sshift)|(?P<asleep>falls asleep)|(?P<awake>wakes up))'

guard_sleep_totals = {}
guard_sleep_minute_count = {}


with open('input.txt') as input_file:
    logs = []
    for line in input_file:
        logs.append(line)
    logs.sort()

guard = None
start_sleep = None
for line in logs:
    match = re.search(re_patt, line)
    minute = int(match.group('minute'))
    guard_id = match.group('guard_id')
    awake = match.group('awake')
    asleep = match.group('asleep')

    if guard_id is not None:
        guard = guard_id
    elif awake:
        if guard not in guard_sleep_minute_count:
            guard_sleep_minute_count[guard] = {}
        guard_sleep_totals[guard] = guard_sleep_totals.get(guard, 0) + minute - start_sleep
        guard_minute_counter = guard_sleep_minute_count.get(guard, {})
        for each_minute in range(start_sleep, minute):
            guard_sleep_minute_count[guard][each_minute] = guard_sleep_minute_count[guard].get(each_minute, 0) + 1
        start_sleep = None
    elif asleep:
        start_sleep = minute

biggest_sleeper = [g for g in guard_sleep_totals if guard_sleep_totals[g] == max(guard_sleep_totals.values())][0]
biggest_sleeper_minutes = guard_sleep_minute_count[biggest_sleeper]
biggest_sleeper_min = [m for m in biggest_sleeper_minutes if biggest_sleeper_minutes[m] == max(biggest_sleeper_minutes.values())][0]

print('Part One: {}'.format(biggest_sleeper_min * int(biggest_sleeper)))

part_two_guard = None
sleepiest_occurrence = 0
print(guard_sleep_minute_count)
for guard in guard_sleep_minute_count:
    sleepiest_minute = max(guard_sleep_minute_count[guard].values())
    if sleepiest_minute > sleepiest_occurrence:
        sleepiest_occurrence = sleepiest_minute
        part_two_guard = guard

sleeper_dict = guard_sleep_minute_count[part_two_guard]
sleepiest_minute = [m for m in sleeper_dict if sleeper_dict[m] == sleepiest_occurrence][0]

print('Part Two: {}'.format(int(part_two_guard) * sleepiest_minute))


