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
def blink(stone: int):
    if stone == 0:
        return [1]
    number_of_digits = get_number_of_digits(stone)
    if number_of_digits % 2 == 0:
        left_stone, right_stone = split_number(number_of_digits, stone)
        return [left_stone, right_stone]
    return [stone * 2024]

@cache
def calculate_number_of_stones(stone: int, remaining_blinks: int):
    if remaining_blinks == 0:
        return 1
    new_stones = blink(stone)
    number_of_stones = 0
    for stone in new_stones:
        number_of_stones += calculate_number_of_stones(stone, remaining_blinks - 1)
    return number_of_stones

number_of_stones = 0
for stone in stones:
    number_of_stones += calculate_number_of_stones(stone, 75)

print('Final number of stones:', number_of_stones)
