import re


def read_input(text):
    crates, instrs = text.split("\n\n")

    crates = crates.split("\n")[:-1][::-1]
    columns = [[] for _ in range(9)]
    for row in crates:
        row = row + " "
        for i, col in enumerate(row[i : i + 4] for i in range(0, len(row), 4)):
            if col == "    ":
                continue
            columns[i].append(col[1])

    instrs = [
        re.search(r"move (\d+) from (\d+) to (\d+)", instr)
        for instr in instrs.split("\n")
    ]
    instrs = [map(int, instr.groups()[0:3]) for instr in instrs]

    return columns, instrs


def part1(inp):
    columns, instrs = inp
    for move, frm, to in instrs:
        for _ in range(move):
            columns[to - 1].append(columns[frm - 1].pop())
    msg = "".join(column[-1] for column in columns)
    return msg


def part2(inp):
    columns, instrs = inp
    for move, frm, to in instrs:
        tmp = []
        for _ in range(move):
            tmp.append(columns[frm - 1].pop())
        columns[to - 1] += tmp[::-1]
    msg = "".join(column[-1] for column in columns)
    return msg
