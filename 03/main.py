import argparse
import re
from collections import namedtuple


CLAIM_SPEC = re.compile(
    r'^#(?P<claim_id>\d+) @ (?P<x_offset>\d+),(?P<y_offset>\d+): (?P<width>\d+)x(?P<height>\d+)$',
)


Claim = namedtuple(
    'Claim',
    [
        'claim_id',
        'x_offset',
        'y_offset',
        'width',
        'height',
    ],
)


def extract_claims(claim_lines):
    claims = []
    for claim_line in claim_lines:
        match = CLAIM_SPEC.match(claim_line)
        claims.append(
            Claim(
                int(match.group('claim_id')),
                int(match.group('x_offset')),
                int(match.group('y_offset')),
                int(match.group('width')),
                int(match.group('height')),
            ),
        )

    return claims


def map_claims(claims):
    claim_map = {}
    for claim in claims:
        x_offset = claim.x_offset
        y_offset = claim.y_offset
        for x in range(claim.width):
            for y in range(claim.height):
                coordinate = (x_offset + x, y_offset + y)
                if coordinate not in claim_map:
                    claim_map[coordinate] = []
                claim_map[coordinate].append(claim.claim_id)

    return claim_map


def contested_claims(claim_map):
    contested_claims = []
    for coordinate, claims in claim_map.items():
        if len(claims) > 1:
            contested_claims.append(coordinate)

    return contested_claims



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'claims_file',
    )
    args = parser.parse_args()
    with open(args.claims_file) as claims_file:
        claims = extract_claims(claims_file.readlines())


    claim_map = map_claims(claims)
    print(len(contested_claims(claim_map)))


if __name__ == '__main__':
	main()
