import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'nums',
		metavar='N',
		type=int,
		nargs='+',
	)
	parser.add_argument(
        '--sum',
        dest='accumulate',
        action='store_const',
        const=sum,
        default=sum,
    )
	args = parser.parse_args()
	print(args.accumulate(args.nums))


if __name__ == '__main__':
	main()
