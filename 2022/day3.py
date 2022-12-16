def read_input(text):
    return text.split()


def part1(inp):
    total = 0
    for rucksack in inp:
        length = len(rucksack) // 2
        half_1 = rucksack[:length]
        half_2 = rucksack[length:]
        item = list(set(half_1) & set(half_2))[0]
        total += prio(item)
    return total


def part2(inp):
    total = 0
    for group in (inp[i : i + 3] for i in range(0, len(inp), 3)):
        item = set(group[0]) & set(group[1]) & set(group[2])
        total += prio(list(item)[0])
    return total


def prio(char):
    ord_ = ord(char)
    if ord_ > 96:
        return ord_ - 96
    else:
        return ord_ - 64 + 26
