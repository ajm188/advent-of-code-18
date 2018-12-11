import argparse
import re


INSTRUCTION = re.compile(r'Step (?P<dependency>.) .* step (?P<step>.) can begin\.')


def extract_dependency_graph(instructions):
    graph = {}
    for instruction in instructions:
        match = INSTRUCTION.match(instruction)
        step, dependency = match.group('step'), match.group('dependency')
        if step not in graph:
            graph[step] = []
        if dependency not in graph:
            graph[dependency] = []

        graph[step].append(dependency)

    return graph


def get_next_step(graph, completed_steps):
    for step in sorted(graph.keys()):
        deps = set(graph[step])
        if deps - completed_steps == set():
            return step


def get_order(graph):
    steps = []
    while graph:
        next_step = get_next_step(graph, set(steps))
        graph.pop(next_step)
        steps.append(next_step)

    return steps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'instructions',
    )
    args = parser.parse_args()
    with open(args.instructions) as instructions:
        graph = extract_dependency_graph(instructions.readlines())

    print(graph)
    print(''.join(get_order(graph)))


if __name__ == '__main__':
	main()
