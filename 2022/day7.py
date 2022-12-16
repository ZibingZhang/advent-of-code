from __future__ import annotations

import functools
import re


class Tree:
    parent: Tree | None
    name: str
    value: int
    children: set[Tree]

    def __init__(self):
        self.children = set()
        self.value = 0

    def cd(self, name):
        if name == "..":
            return self.parent
        for child in self.children:
            if child.name == name:
                return child

    @functools.cached_property
    def size(self):
        total = 0
        for child in self.children:
            total += child.size
        return total + self.value


def read_input(text):
    tree = root = Tree()
    for line in text.split("\n"):
        if match := re.search(r"dir (\w+)", line):
            name = match.groups()[0]
            new_tree = Tree()
            new_tree.parent = tree
            new_tree.name = name
            tree.children.add(new_tree)
        elif match := re.search(r"(\d+) (.+)", line):
            value, name = match.groups()[:2]
            new_tree = Tree()
            new_tree.parent = tree
            new_tree.name = name
            new_tree.value = int(value)
            tree.children.add(new_tree)
        elif line == "$ cd /":
            tree = root
        elif match := re.search(r"\$ cd ([.\w]+)", line):
            tree = tree.cd(match.groups()[0])

    return root


def part1(inp):
    return sum(part1_recur(child) for child in inp.children)


def part1_recur(inp):
    total = 0
    if inp.size < 100000 and inp.value == 0:
        total += inp.size()
    return total + sum(map(part1_recur, inp.children))


def part2(inp):
    space = 30000000 - 70000000 + inp.size
    dirs = valid_dirs(inp, space)
    min_dir = inp
    for dir_ in dirs:
        if dir_.size < min_dir.size:
            min_dir = dir_
    return min_dir.size


def valid_dirs(inp, space):
    valid_child_dirs = [
        dir_ for child in inp.children for dir_ in valid_dirs(child, space)
    ]
    if inp.size >= space and inp.value == 0:
        valid_child_dirs.append(inp)
    return valid_child_dirs
