import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'nums',
        metavar='N',
        type=int,
        nargs='+',
    )
    args = parser.parse_args()
    frequency = 0
    first_repitition = None
    frequencies = set([0])
    while first_repitition is None:
        for n in args.nums:
            frequency += n
            if frequency not in frequencies:
                frequencies.add(frequency)
            else:
                if first_repitition is None:
                    first_repitition = frequency

    print(sum(args.nums))
    print(first_repitition)


if __name__ == '__main__':
	main()
