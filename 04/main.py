import argparse
import re
from collections import defaultdict


GUARD = re.compile(r'Guard #(?P<guard_id>\d+)')


def extract_minute_from_log_line(log_line):
    separator = log_line.index(':') + 1
    return int(log_line[separator:separator + 2])


def sleep_logs(log_lines):
    sleep_logs = defaultdict(int)
    minutes_per_guard = {}
    guard_on_duty, minute_asleep = None, None
    for log_line in log_lines:
        if 'begins shift' in log_line:
            guard_on_duty = int(GUARD.search(log_line).group('guard_id'))
        elif 'falls asleep' in log_line:
            minute_asleep = extract_minute_from_log_line(log_line)
        elif 'wakes up' in log_line:
            minute_awake = extract_minute_from_log_line(log_line)
            nap_length = minute_awake - minute_asleep
            if guard_on_duty not in minutes_per_guard:
                minutes_per_guard[guard_on_duty] = defaultdict(int)
            for i in range(nap_length):
                minutes_per_guard[guard_on_duty][minute_asleep + i] += 1

            sleep_logs[guard_on_duty] += nap_length

    return sleep_logs, minutes_per_guard


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'logs',
    )
    args = parser.parse_args()
    with open(args.logs) as logs:
        lines_by_timestamp = {
            line[0:line.index(']')]: line
            for line in logs.readlines()
        }

    log_lines = [
        lines_by_timestamp[line_ts]
        for line_ts in sorted(lines_by_timestamp.keys())
    ]
    sleep_lengths, minutes_per_guard = sleep_logs(log_lines)
    worst_guard, longest_nap = None, 0
    for guard, nap_length in sleep_lengths.items():
        if nap_length > longest_nap:
            longest_nap = nap_length
            worst_guard = guard

    worst_minute, times_asleep_in_worst_minute = None, 0
    for minute, times_asleep in minutes_per_guard[worst_guard].items():
        if times_asleep > times_asleep_in_worst_minute:
            times_asleep_in_worst_minute = times_asleep
            worst_minute = minute

    print(worst_guard * worst_minute)


if __name__ == '__main__':
	main()
