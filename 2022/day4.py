def read_input(text):
    pairs = text.split()
    return [
        (split_zone(range_1), split_zone(range_2))
        for range_1, range_2 in (pair.split(",") for pair in pairs)
    ]


def split_zone(range_):
    range_ = range_.split("-")
    return int(range_[0]), int(range_[1])


def part1(inp):
    total = 0
    for range_1, range_2 in inp:
        if (range_1[0] <= range_2[0] and range_1[1] >= range_2[1]) or (
            range_2[0] <= range_1[0] and range_2[1] >= range_1[1]
        ):
            total += 1
    return total


def part2(inp):
    total = 0
    for range_1, range_2 in inp:
        if set(range(range_1[0], range_1[1] + 1)) & set(
            range(range_2[0], range_2[1] + 1)
        ):
            total += 1
    return total
