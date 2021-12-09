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


def part_2():
    df = pd.read_csv("problem_6/input.txt", header=None).transpose()
    df[1] = df[0]
    df = df.groupby(0).count().fillna(0)
    df.loc[6] = 0
    df.loc[7] = 0
    df.loc[8] = 0
    df.loc[9] = 0
    df.loc[0] = 0
    df = df.reindex(range(10))
    simulations = 256
    while simulations > 0:
        df.loc[9] = df.loc[0]
        df.loc[7] += df.loc[0]
        df = df.shift(-1).fillna(0)
        simulations -= 1
    print(df.sum().astype(str))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
