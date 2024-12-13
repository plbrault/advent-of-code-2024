import math
from datetime import datetime

stones : [int]

with open('input.txt') as file:
    line = file.readline()
    stones = [int(number) for number in line.split(' ')]

def get_number_of_digits(number):
    return int(math.log10(number)) + 1

def split_number(number_of_digits, number):
    return number // 10 ** (number_of_digits // 2), number % 10 ** (number_of_digits // 2)

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            number_of_digits = get_number_of_digits(stone)
            if number_of_digits % 2 == 0:
                left_stone, right_stone = split_number(number_of_digits, stone)
                new_stones.append(left_stone)
                new_stones.append(right_stone)
            else:
                new_stones.append(stone * 2024)
    return new_stones

for i in range(25):
    print('Blink #', i)
    stones = blink(stones)

print('Number of stones after 25 blinks:', len(stones))

last_blink = datetime.now()
for i in range(50):
    print('Blink #', i + 25)
    stones = blink(stones)
    print('Number of stones:', len(stones))
    print('Blink duration:', datetime.now() - last_blink)

print('Number of stones after 75 blinks:', len(stones))
