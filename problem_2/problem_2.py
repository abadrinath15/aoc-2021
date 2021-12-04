def part_1():
    x_pos = 0
    y_pos = 0
    with open('input.txt') as file:
        while (line :=  file.readline().rstrip().split(' '))  != ['']:
            match line[0], int(line[1]):
                case 'forward', x:
                    x_pos  +=  x
                case 'down', y:
                    y_pos += y
                case 'up', y:
                    y_pos -= y 

    print(x_pos * y_pos)



def part_2():
    with open('input.txt') as file:
        x_pos = 0
        y_pos = 0
        aim = 0
        while(line := file.readline().rstrip().split(' ')) != ['']:
            match line[0], int(line[1]):
                case 'forward', x:
                    x_pos += x 
                    y_pos += aim * x
                case 'down', x:
                    aim += x
                case 'up', x:
                    aim -= x

        print(x_pos * y_pos)
                
                    

def main():
    part_1()
    part_2()


if __name__ == '__main__':
    main()
