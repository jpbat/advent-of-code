from collections import namedtuple


Record = namedtuple('Record', ['minute', 'guard_id', 'action'])


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def convert_to_records(lines):

    records = []
    guard_id = None
    for line in lines:

        splitted = line.replace('#', '').replace('[', '').replace(']', '').split()

        if '#' in line:
            guard_id = int(splitted[3])
            continue

        minute = int(splitted[1].split(':')[1])

        if 'wakes up' in line:
            action = 'wake'
        else:
            action = 'sleep'

        records.append(Record(minute, guard_id, action))

    return records


def main():

    lines = read_input()
    lines.sort()
    records = convert_to_records(lines)

    sleep_times = {}

    for i in range(len(records)):

        if records[i].guard_id not in sleep_times:
            sleep_times[records[i].guard_id] = {'total': 0}

        if records[i].action == 'wake':

            start_sleep = records[i - 1].minute
            end_sleep = records[i].minute

            for minute in range(start_sleep, end_sleep):
                if minute not in sleep_times[records[i].guard_id]:
                    sleep_times[records[i].guard_id][minute] = 0
                sleep_times[records[i].guard_id][minute] += 1

            sleep_times[records[i].guard_id]['total'] += end_sleep - start_sleep

    sleepy_guard = None
    sleepy_minute = None

    for guard_id, minute_dict in sleep_times.items():

        for minute_key, value in minute_dict.items():

            if minute_key == 'total':
                continue

            if sleepy_guard is None or sleep_times[guard_id][minute_key] > sleep_times[sleepy_guard][sleepy_minute]:
                sleepy_guard = guard_id
                sleepy_minute = minute_key

    print (sleepy_guard * sleepy_minute)


if __name__ == '__main__':
    main()
