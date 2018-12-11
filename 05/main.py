import argparse


def react(polymer):
    for i, c in enumerate(list(polymer[:-1])):
        if (
            c.lower() == polymer[i+1].lower() and \
            c != polymer[i+1]
        ):
            return polymer[:i] + polymer[i+2:]

    return polymer


def fully_react(polymer):
    current_polymer = polymer
    stop = False
    while not stop:
        old_polymer, current_polymer = current_polymer, react(current_polymer)
        stop = (old_polymer == current_polymer)

    return current_polymer
            

def extract_unit(polymer, unit):
    lower_removed = polymer.replace(unit.lower(), '')
    return lower_removed.replace(unit.upper(), '')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'polymer',
    )
    args = parser.parse_args()
    print(len(fully_react(args.polymer)))

    shortest = len(args.polymer)
    for c in set(args.polymer.lower()):
        reacted = fully_react(extract_unit(args.polymer, c))
        if len(reacted) < shortest:
            shortest = len(reacted)

    print(shortest)


if __name__ == '__main__':
	main()
