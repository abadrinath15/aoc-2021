import pandas as pd

def part_1():
    coords = list(pd.read_csv('input.txt', header=None, dtype={0:str}).values.transpose())
    coords = [list(x) for x in coords[0]]
    coords = pd.DataFrame(coords).astype(int)
    anti_coords = (coords + 1).mod(2)
    res = int(''.join(str(x) for x in coords.mode().values[0]), base=2)
    anti_res = int(''.join(str(x) for x in anti_coords.mode().values[0]), base=2)
    print(res * anti_res)

    

def main():
    part_1()

if __name__ ==  '__main__':
    main()
