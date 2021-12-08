import pandas as pd
import numpy as np
from typing import Tuple, List


class BingoBoard:
    def __init__(self, board: pd.DataFrame) -> None:
        self.drawn_numbers_sum = 0
        self.lookup_map = {}
        for row_num, row in board.iterrows():
            for col_num, val in row.iteritems():
                self.lookup_map[val] = (row_num, col_num)
        self.board = np.zeros(board.shape)

    def play_turn(self, number: int) -> Tuple[bool, int]:
        self.drawn_numbers_sum += number
        if number in self.lookup_map:
            coords = self.lookup_map.pop(number)
            self.board[coords] = 1
            if any(self.board.sum(0) == len(self.board)) or any(
                self.board.sum(1) == len(self.board)
            ):
                return True, sum(value for value in self.lookup_map) * number
        return False, -1


def get_input() -> Tuple[List[int], List[BingoBoard]]:
    input_file = "problem_4/input.txt"
    with open(input_file) as fp:
        contents = fp.read().split("\n\n")

    list_iter = iter(contents)
    boards: List[BingoBoard] = []
    draws = [int(x) for x in next(list_iter).split(",")]
    while True:
        try:
            new_board = next(list_iter).replace("\n", " ")
            new_board_list = [int(x) for x in new_board.split(" ") if x != ""]
            boards.append(
                BingoBoard(pd.DataFrame(np.array(new_board_list).reshape((5, 5))))
            )
        except StopIteration:
            break

    return draws, boards


def part_1(draws, boards):
    for bingo_piece in draws:
        for board in boards:
            done, score = board.play_turn(bingo_piece)
            if done:
                print(score)
                return


def part_2(draws, boards: List[BingoBoard]):
    for bingo_piece in draws:
        new_list = []
        for x in boards:
            res, sum = x.play_turn(bingo_piece)
            if res:
                continue
            new_list.append(x)
        if len(new_list) == 0:
            print(sum)
            return
        boards = new_list


def main():
    draws, boards = get_input()
    part_1(draws, boards)
    part_2(draws, boards)


if __name__ == "__main__":
    main()
