def read_input(text):
    return [row.split(" ") for row in text.split("\n")]


def part1(inp):
    score = 0
    for them, me in inp:
        score += {"X": 1, "Y": 2, "Z": 3}[me]
        if (
                (them == "A" and me == "X")
                or (them == "B" and me == "Y")
                or (them == "C" and me == "Z")
        ):
            score += 3
        elif (
                (them == "A" and me == "Y")
                or (them == "B" and me == "Z")
                or (them == "C" and me == "X")
        ):
            score += 6
    return score


def part2(inp):
    score = 0
    for them, result in inp:
        if result == "X":
            me = {
                "A": "Z",
                "B": "X",
                "C": "Y",
            }[them]
        elif result == "Y":
            score += 3
            me = {
                "A": "X",
                "B": "Y",
                "C": "Z",
            }[them]
        else:
            score += 6
            me = {
                "A": "Y",
                "B": "Z",
                "C": "X",
            }[them]
        score += {"X": 1, "Y": 2, "Z": 3}[me]
    return score
