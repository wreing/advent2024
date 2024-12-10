# This is a sample Python script.

from day01 import  day01_1, day01_2
from day02 import  day02_1, day02_2
from day03 import  day03_1, day03_2

if __name__ == '__main__':
    day = '03'
    file = f'inputFiles/{day}_1.txt'
    with open(file, 'r') as file:
        content = file.read()

    match day:
        case '01':
            print('part 1 solution')
            print(day01_1(content))
            print('part 2 solution')
            print(day01_2(content))
        case '02':
            print('part 1 solution')
            print(day02_1(content))
            print('part 2 solution')
            print(day02_2(content))
        case '03':
            print('part 1 solution')
            print(day03_1(content))
            print('part 2 solution')
            print(day03_2(content))
