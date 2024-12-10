"""Solution for AOC 2024 day 9"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        disk = []
        position = 0
        for (i, size) in enumerate(int(x) for x in file.read().strip()):
            file_id = i // 2 if i % 2 == 0 else -1
            disk += [(position, file_id, size)]
            position += size
        return disk


def solve1(disk):
    """Solve part 1"""
    cells = []
    for (_, file_id, size) in disk:
        cells += [file_id] * size
    offset, offset_from_end = 0, len(cells) - 1
    while offset < offset_from_end:
        if cells[offset] == -1:
            cells[offset], cells[offset_from_end] = cells[offset_from_end], cells[offset]
            while cells[offset_from_end] == -1:
                offset_from_end -= 1
        offset += 1
    return sum(offset * cell for (offset, cell) in enumerate(cells) if cell != -1)


def solve2(disk):
    """Solve part 2"""
    defrag = list(disk)
    for file_id in [file_id for (position, file_id, file_size) in disk if file_id != -1][::-1]:
        file_slice = [i for (i, f) in enumerate(defrag) if f[1] == file_id][0]
        (position, file_id, file_size) = defrag[file_slice]
        curr_slice = 0
        while True:
            if curr_slice == file_slice:
                # cannot move this file it anywhere
                break
            if defrag[curr_slice][1] != -1 or defrag[curr_slice][2] < file_size:
                curr_slice += 1
                continue
            # move the file slice to its new position
            defrag = defrag[:curr_slice] \
                     + [(defrag[curr_slice][0], file_id, file_size)] \
                     + ([(defrag[curr_slice][0] + file_size, -1, defrag[curr_slice][2] - file_size)]
                          if defrag[curr_slice][2] - file_size > 0 else []) \
                     + defrag[curr_slice+1:file_slice] \
                     + defrag[file_slice+1:]
            break

    return sum(sum((position + k) * file_id for k in range(file_size))
               for (position, file_id, file_size) in defrag
               if file_id != -1)


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 09:', solve1(parsed), solve2(parsed))
