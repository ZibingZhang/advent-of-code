def read_input(text):
    elves = text.split("\n\n")
    return [[int(food) for food in elf.split("\n")] for elf in elves]


def part1(inp):
    return max(sum(elf) for elf in inp)


def part2(inp):
    return sum(sorted((sum(elf) for elf in inp), reverse=True)[:3])
