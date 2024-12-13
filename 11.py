
from dataclasses import dataclass
import math

NUMBER_OF_BLINKS = 25

@dataclass
class Stone:
    value: int
    remaining_blinks: int

stones : [Stone]

with open('input.txt') as file:
    line = file.readline()
    stones = [Stone(int(value), NUMBER_OF_BLINKS) for value in line.split(' ')]

def get_number_of_digits(number):
    return int(math.log10(number)) + 1

def split_number(number_of_digits, number):
    return number // 10 ** (number_of_digits // 2), number % 10 ** (number_of_digits // 2)

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone.remaining_blinks == 0:
            new_stones.append(stone)
        elif stone.value == 0:
            new_stones.append(Stone(1, stone.remaining_blinks - 1))
        else:
            number_of_digits = get_number_of_digits(stone.value)
            if number_of_digits % 2 == 0:
                left_value, right_value = split_number(number_of_digits, stone.value)
                new_stones.append(
                    Stone(
                        left_value,
                        stone.remaining_blinks - 1
                    )
                )
                new_stones.append(
                    Stone(
                        right_value,
                        stone.remaining_blinks - 1
                    )
                )
            else:
                new_stones.append(
                    Stone(
                        stone.value * 2024,
                        stone.remaining_blinks - 1
                    )
                )
    return new_stones

for i in range(NUMBER_OF_BLINKS):
    stones = blink(stones)

print('Final number of stones:', len(stones))
