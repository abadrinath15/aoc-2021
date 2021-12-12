from typing import FrozenSet, List, Set, Dict


def part_1(filename):
    counts = 0
    for line in open(filename):
        counts += sum(
            1 if len(x) in {2, 4, 3, 7} else 0 for x in line.split(" | ")[1].split()
        )

    print(counts)


def part_2(filename):
    def entry_to_nums(display: List[str]) -> Dict[FrozenSet[str], int]:
        missing_ones = []
        missing_twos = []
        for disp in display:
            match len(disp):
                case 2:
                    one = frozenset(disp)
                case 4:
                    four = frozenset(disp)
                case 3:
                    seven = frozenset(disp)
                case 7:
                    eight = frozenset(disp)
                case 6:
                    missing_ones.append(frozenset(disp))
                case 5:
                    missing_twos.append(frozenset(disp))

        for x in missing_ones:
            if len(x & seven) == 2:
                six = x
                missing_ones.remove(x)
                break

        for x in missing_twos:
            if len(six - x) == 1:
                five = x
                missing_twos.remove(x)
                break

        for x in missing_ones:
            if len(x - five) == 1:
                nine = x
                missing_ones.remove(x)
                break

        zero = missing_ones.pop()

        for x in missing_twos:
            if len(nine - x) == 1:
                three = x
                missing_twos.remove(x)
                break

        two = missing_twos.pop()

        return {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
        }

    total = 0
    for line in open(filename):
        line_split = line.split(" | ")
        signals = line_split[0].split()
        output = [frozenset(x) for x in line_split[1].split()]
        entry_map = entry_to_nums(signals)
        total += (
            1000 * entry_map[output[0]]
            + 100 * entry_map[output[1]]
            + 10 * entry_map[output[2]]
            + entry_map[output[3]]
        )

    print(total)


def main():
    part_2("problem_8/input.txt")


if __name__ == "__main__":
    main()
