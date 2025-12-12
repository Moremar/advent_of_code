"""Solution for AOC 2025 day 9"""
import matplotlib.pyplot as plt


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        red_tiles = []
        for line in file.readlines():
            x, y = line.strip().split(',')
            red_tiles.append((int(x), int(y)))
        return red_tiles


def solve1(red_tiles):
    """Solve part 1"""
    max_area = 0
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            t1, t2 = red_tiles[i], red_tiles[j]
            max_area = max(max_area, (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1))
    return max_area


def is_fully_green(t1, t2, green_lines_x, green_lines_y):
    """Return True if the rectangle formed by t1 and t2 is fully in the green area"""
    # The generic case is quite hard to check, so we plotted the shape to see what needs to be checked.
    # check that the other 2 edges of the rectangle are in the green area
    # for that, we ensure that there is a green line in all 4 directions from them
    for t in [(t1[0], t2[1]), (t2[0], t1[1])]:
        up_ok, down_ok, left_ok, right_ok = False, False, False, False
        for (x1, x2, y) in green_lines_x:
            if x1 <= t[0] <= x2 and y >= t[1]:
                up_ok = True
            if x1 <= t[0] <= x2 and y <= t[1]:
                down_ok = True
        for (y1, y2, x) in green_lines_y:
            if y1 <= t[1] <= y2 and x >= t[0]:
                right_ok = True
            if y1 <= t[1] <= y2 and x <= t[0]:
                left_ok = True
        if not up_ok or not down_ok or not left_ok or not right_ok:
            return False
    # with the knowledge of our specific form, we see that a rectangle is fully in the green area
    # if it is not crossed by any green line
    for (x1, x2, y) in green_lines_x:
        if (x1 < t1[0] < x2 or x1 < t2[0] < x2) and (t1[1] < y < t2[1] or t2[1] < y < t1[1]):
            return False
    for (y1, y2, x) in green_lines_y:
        if (y1 < t1[1] < y2 or y1 < t2[1] < y2) and (t1[0] < x < t2[0] or t2[0] < x < t1[0]):
            return False
    return True


def solve2(red_tiles):
    """Solve part 2"""
    green_lines = {(red_tiles[i], red_tiles[(i+1) % len(red_tiles)]) for i in range(len(red_tiles))}
    green_lines_x = {(min(t1[0], t2[0]), max(t1[0], t2[0]), t1[1]) for (t1, t2) in green_lines if t1[0] != t2[0]}
    green_lines_y = {(min(t1[1], t2[1]), max(t1[1], t2[1]), t1[0]) for (t1, t2) in green_lines if t1[1] != t2[1]}
    max_area = 0
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            t1, t2 = red_tiles[i], red_tiles[j]
            area = (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
            if area > max_area:
                if is_fully_green(t1, t2, green_lines_x, green_lines_y):
                    max_area = area
    return max_area


def plot_green_lines(red_tiles):
    """Plot the green lines defined by the red tiles"""
    segments = [(red_tiles[i], red_tiles[i + 1]) for i in range(len(red_tiles) - 1)]
    for (x1, y1), (x2, y2) in segments:
        plt.plot([x1, x2], [y1, y2])
    plt.axis('equal')  # optional: keeps proportions correct
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    parsed = parse('data.txt')
    #plot_green_lines(parsed)
    print('Day 9:', solve1(parsed), solve2(parsed))
