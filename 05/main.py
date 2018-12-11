import argparse


def react(polymer):
    for i, c in enumerate(list(polymer[:-1])):
        if (
            c.lower() == polymer[i+1].lower() and \
            c != polymer[i+1]
        ):
            return polymer[:i] + polymer[i+2:]

    return polymer
            


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'polymer',
    )
    args = parser.parse_args()

    current_polymer = args.polymer
    stop = False
    while not stop:
        old_polymer, current_polymer = current_polymer, react(current_polymer)
        stop = (old_polymer == current_polymer)

    print(len(current_polymer))


if __name__ == '__main__':
	main()
