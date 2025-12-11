"""Solution for AOC 2025 day 11"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        connections = {}
        for line in file.readlines():
            source, outputs = line.strip().split(': ')
            connections[source] = set(outputs.split(' '))
        return connections


def get_path_to_out(node, connections, cache):
    """Recursive function to count the number of paths from a node to the out node"""
    if node not in cache:
        cache[node] = sum(get_path_to_out(next_node, connections, cache) for next_node in connections[node])
    return cache[node]


def solve1(connections):
    """Solve part 1"""
    return get_path_to_out('you', connections, {'out': 1})


def get_path_to_out2(node, connections, dac_seen, fft_seen, cache):
    """Recursive function to count the number of paths from a node to the out node visiting dac and fft nodes"""
    if (node, dac_seen, fft_seen) not in cache:
        count = 0
        for next_node in connections[node]:
            next_dac_seen = dac_seen or next_node == 'dac'
            next_fft_seen = fft_seen or next_node == 'fft'
            count += get_path_to_out2(next_node, connections, next_dac_seen, next_fft_seen, cache)
        cache[(node, dac_seen, fft_seen)] = count
    return cache[(node, dac_seen, fft_seen)]


def solve2(connections):
    """Solve part 2"""
    cache = {('out', True, True): 1, ('out', False, True): 0, ('out', True, False): 0, ('out', False, False): 0}
    return get_path_to_out2('svr', connections, False, False, cache)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 11:', solve1(parsed), solve2(parsed))
