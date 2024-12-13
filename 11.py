import math
from datetime import datetime
from functools import cache

stones : [int]

with open('input.txt') as file:
    line = file.readline()
    stones = [int(number) for number in line.split(' ')]

def get_number_of_digits(number):
    return int(math.log10(number)) + 1

def split_number(number_of_digits, number):
    return number // 10 ** (number_of_digits // 2), number % 10 ** (number_of_digits // 2)

@cache
def blink(stone):
    if stone == 0:
        return [1]
    number_of_digits = get_number_of_digits(stone)
    if number_of_digits % 2 == 0:
        left_stone, right_stone = split_number(number_of_digits, stone)
        return [left_stone, right_stone]
    return [stone * 2024]

def compute(stones):
    new_stones = []
    for stone in stones:
        new_stones += blink(stone)
    return new_stones

for i in range(25):
    print('Blink #', i)
    stones = compute(stones)

print('Final number of stones:', len(stones))
