import pandas as pd

def part_1():
    coords = list(pd.read_csv('input.txt', header=None, dtype={0:str}).values.transpose())
    coords = [list(x) for x in coords[0]]
    coords = pd.DataFrame(coords).astype(int)
    anti_coords = (coords + 1).mod(2)
    res = int(''.join(str(x) for x in coords.mode().values[0]), base=2)
    anti_res = int(''.join(str(x) for x in anti_coords.mode().values[0]), base=2)
    print(res * anti_res)

def part_2():
    coords = list(pd.read_csv('input.txt', header=None, dtype={0:str}).values.transpose())
    coords = [list(x) for x in coords[0]]
    coords = pd.DataFrame(coords).astype(int)                                                 
    anti_coords=coords.copy()
    for i in range(len(coords.columns)):
        freq_val = coords.iloc[:, i].mode().tail(1).iloc[0]
        coords = coords[coords.iloc[:, i] == freq_val]
    for i in range(len(anti_coords.columns)):
        if len(anti_coords) == 1:
            break
        freq_val = anti_coords.iloc[:, i].mode().tail(1).iloc[0]
        anti_coords = anti_coords[anti_coords.iloc[:, i] != freq_val]


    print(int(''.join(str(x) for x in coords.values[0]), base=2) *  int(''.join(str(x) for x in anti_coords.values[0]), base=2))


def main():
    part_2()

if __name__ ==  '__main__':
    main()
