# This is a sample Python script.

from day01 import  day01_1, day01_2

if __name__ == '__main__':
    day = '01'
    part = '1'
    file=f'inputFiles/{day}_{part}.txt'
    with open(file, 'r') as file:
        content = file.read()

    match day:
        case '01':
            print('part 1 solution')
            print(day01_1(content))
            print('part 2 solution')
            print(day01_2(content))

