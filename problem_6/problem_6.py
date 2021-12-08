import pandas as pd
import numpy as np


def part_1():
    arr = pd.read_csv("problem_6/input.txt", header=None).values
    simulate = 80
    while simulate > 0:
        num_zero = len(arr) - np.count_nonzero(arr)
        arr = np.append(arr, [9] * num_zero)
        arr = np.where(arr == 0, 7, arr)
        arr = arr - 1
        simulate -= 1
    print(len(arr))


def main():
    part_1()


if __name__ == "__main__":
    main()
