from collections import Counter


def part_1():
    counts = Counter()
    with open("problem_5/input.txt") as file:
        for line in file:
            start_coord, _, end_coord = line.split(" ")
            x_0, y_0 = [int(a) for a in start_coord.split(",")]
            x_1, y_1 = [int(a) for a in end_coord.split(",")]
            if x_0 == x_1:
                counts.update((x_0, y) for y in range(min(y_0, y_1), max(y_0, y_1) + 1))
            elif y_0 == y_1:
                counts.update((x, y_0) for x in range(min(x_0, x_1), max(x_0, x_1) + 1))
    greater_2 = 0
    for v in counts.values():
        if v >= 2:
            greater_2 += 1

    print(greater_2)


def part_2():
    counts = Counter()
    with open("problem_5/input.txt") as file:
        for line in file:
            start_coord, _, end_coord = line.split(" ")
            x_0, y_0 = [int(a) for a in start_coord.split(",")]
            x_1, y_1 = [int(a) for a in end_coord.split(",")]
            if x_0 == x_1:
                counts.update((x_0, y) for y in range(min(y_0, y_1), max(y_0, y_1) + 1))
            elif y_0 == y_1:
                counts.update((x, y_0) for x in range(min(x_0, x_1), max(x_0, x_1) + 1))
            else:
                slope = (y_1 - y_0) / (x_1 - x_0)
                stride = 1 if x_1 >= x_0 else -1
                counts.update(
                    (x_0 + i, int(y_0 + slope * i))
                    for i in range(0, x_1 - x_0 + stride, stride)
                )
    greater_2 = 0
    for v in counts.values():
        if v >= 2:
            greater_2 += 1

    print(greater_2)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
