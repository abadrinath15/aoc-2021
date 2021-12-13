from collections import deque
from statistics import median


def part_1(filename: str) -> None:
    correct_ending = {")": "(", "}": "{", "]": "[", ">": "<"}
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in open(filename):
        syntax_stack = deque()
        for char in line:
            if char in correct_ending:
                start = syntax_stack.pop()
                if correct_ending[char] != start:
                    score += score_map[char]
                    break
            else:
                syntax_stack.append(char)
    print(score)


def part_2(filename: str) -> None:
    correct_ending = {")": "(", "}": "{", "]": "[", ">": "<"}
    correct_starting = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in open(filename):
        score = 0
        syntax_stack = deque()
        for char in line:
            if char == "\n":
                break
            if char in correct_ending:
                start = syntax_stack.pop()
                if correct_ending[char] != start:
                    syntax_stack = deque()
                    break
            else:
                syntax_stack.append(char)
        while len(syntax_stack) > 0:
            score = 5 * score + correct_starting[syntax_stack.pop()]
        if score != 0:
            scores.append(score)

    print(median(scores))


def main():
    part_1("problem_10/input.txt")
    part_2("problem_10/input.txt")


if __name__ == "__main__":
    main()
