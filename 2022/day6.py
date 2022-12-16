def read_input(text):
    return text


def part1(inp):
    for i in range(len(inp)):
        if len(set(inp[i : i + 4])) == 4:
            return i + 4


def part2(inp):
    for i in range(len(inp)):
        if len(set(inp[i : i + 14])) == 14:
            return i + 14
