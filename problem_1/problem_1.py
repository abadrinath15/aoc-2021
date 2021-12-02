import pandas as pd

def part_1():
    input_df = pd.read_csv('input1.txt', header=None)
    print((input_df.diff() > 0).sum())

def part_2():
    input_df: pd.DataFrame = pd.read_csv('input1.txt', header=None)
    print((input_df.rolling(3).sum().diff() > 0).sum())


def main():
   part_1()
   part_2()

if __name__ == '__main__':
    main()
