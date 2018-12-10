import argparse


def checksum(ids):
    two_count, three_count = 0, 0
    for id_str in ids:
        counter = {}
        for c in id_str:
            counter[c] = counter.get(c, 0) + 1

        counts = counter.values()
        if 2 in counts:
            two_count += 1
        if 3 in counts:
            three_count += 1

    return two_count * three_count


def diff(id1, id2):
    found_diff = False
    common = ''
    for c1, c2 in zip(id1, id2):
        if c1 != c2:
            if found_diff:
                return ''
            found_diff = True
        else:
            common += c1
    return common


def find_common(ids):
    for i, id1 in enumerate(ids):
        for id2 in (ids[:i] + ids[i+1:]):
            common = diff(id1, id2)
            if len(id1) - len(common) == 1:
                return common


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'ids',
        metavar='ID',
        nargs='+',
    )
    args = parser.parse_args()
    print(checksum(args.ids))
    print(find_common(args.ids))


if __name__ == '__main__':
	main()
