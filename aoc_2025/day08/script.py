"""Solution for AOC 2025 day 8"""
from Point3D import Point3D


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        boxes = []
        for line in file.readlines():
            x, y, z = line.strip().split(',')
            boxes.append(Point3D(int(x), int(y), int(z)))
        return boxes


def connect_boxes(boxes, max_junctions=None):
    """Create up to the specified number of junctions between boxes, or until we have a single circuit"""
    square_distances = dict()
    for i in range(len(boxes)-1):
        for j in range(i+1, len(boxes)):
            p1, p2 = boxes[i], boxes[j]
            dist2 = p1.dist2(p2)
            square_distances[dist2] = (p1, p2)  # no need to create a map, no pairs are at the same distance
    # connect the closest boxes to create circuits
    circuits = dict()
    step = 0
    ordered_dist = sorted(i for i in square_distances)
    for dist in ordered_dist:
        step += 1
        p1, p2 = square_distances[dist]
        found_circuit_id = None
        for circuit_id in circuits:
            if p1 in circuits[circuit_id] and p2 in circuits[circuit_id]:
                # both boxes are already in the same circuit, no changes to the circuits
                found_circuit_id = circuit_id
                break
            if p1 in circuits[circuit_id] or p2 in circuits[circuit_id]:
                if not found_circuit_id:
                    circuits[circuit_id].add(p1)
                    circuits[circuit_id].add(p2)
                    found_circuit_id = circuit_id
                else:
                    circuits[found_circuit_id] = circuits[found_circuit_id].union(circuits[circuit_id])
                    del circuits[circuit_id]
                    break
        if not found_circuit_id:
            circuits[dist] = {p1, p2}    # use the square distance of the connected boxes as circuit_id for uniqueness
        # exit if the specified max number of junctions was added (part 1)
        if step == max_junctions:
            circuit_sizes = sorted(len(circuits[circuit_id]) for circuit_id in circuits)
            return circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3]
        # exist if we got a single circuit containing all boxes (part 2)
        if len(circuits) == 1:
            for circuit_id in circuits:
                if len(circuits[circuit_id]) == len(boxes):
                    return p1.x * p2.x


def solve1(boxes, max_junctions):
    return connect_boxes(boxes, max_junctions)


def solve2(boxes):
    return connect_boxes(boxes)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 8:', solve1(parsed, 1000), solve2(parsed))
