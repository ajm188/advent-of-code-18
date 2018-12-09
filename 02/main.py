import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'ids',
        metavar='ID',
        nargs='+',
    )
    args = parser.parse_args()
    two_count, three_count = 0, 0
    for id_str in args.ids:
        counter = {}
        for c in id_str:
            counter[c] = counter.get(c, 0) + 1

        counts = counter.values()
        if 2 in counts:
            two_count += 1
        if 3 in counts:
            three_count += 1

    print(two_count * three_count)


if __name__ == '__main__':
	main()
