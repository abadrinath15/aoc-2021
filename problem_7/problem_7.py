import pandas as pd
import numpy as np


def part_1():
    df = pd.read_csv("problem_7/input.txt", header=None).transpose()
    df_1 = df.transpose()
    df_1 = pd.concat([df_1] * (df_1.shape[1]))
    print(min(np.abs(df.values - df_1.values).sum(axis=0)))


def part_2():
    input_arr = pd.read_csv("problem_7/input.txt", header=None).values[0]
    arr = np.concatenate(
        [[range(min(input_arr), max(input_arr) + 1)] for _ in range(len(input_arr))]
    )
    input_arr = np.reshape(np.transpose(input_arr), (len(input_arr), -1))
    res = np.absolute(input_arr - arr)
    print(res)
    print(res * (res + 1) / 2)
    print(min((res * (res + 1) / 2).sum(axis=0)))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
