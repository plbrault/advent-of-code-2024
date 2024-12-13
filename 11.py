
from dataclasses import dataclass
import math

MAX_BLINKS = 25

@dataclass
class Stone:
    value: int
    remaining_blinks: int

stones : [Stone]

with open('input.txt') as file:
    line = file.readline()
    stones = [Stone(int(value), MAX_BLINKS) for value in line.split(' ')]

def get_number_of_digits(number):
    if number == 0:
        return 1
    return int(math.log10(number)) + 1

def split_number(number_of_digits, number):
    return number // 10 ** (number_of_digits // 2), number % 10 ** (number_of_digits // 2)

precomputations = {}

debug = False

def blink(stones: [Stone]):
    new_stones = []
    for stone in stones:
        if stone.remaining_blinks == 0:
            new_stones.append(stone)
        else:
            if (
                stone.value in precomputations
                and precomputations[stone.value][0] <= stone.remaining_blinks
            ):
                blink_count, new_stone_values = precomputations[stone.value]
                remaining_blinks = stone.remaining_blinks - blink_count
                new_stones += [
                    Stone(new_stone_value, remaining_blinks)
                        for new_stone_value in new_stone_values
                ]
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

for i in range(1, 8):
    debug = True
    stone = Stone(i * 2024, MAX_BLINKS - 1)
    blink_count = 1
    new_stones = [stone]
    while len([
        new_stone for new_stone
            in new_stones
            if get_number_of_digits(new_stone.value) > 1
    ]) > 0:
        new_stones = blink(new_stones)
        blink_count += 1
    precomputations[i] = (blink_count, [new_stone.value for new_stone in new_stones])
precomputations[0] = (precomputations[1][0] + 1, precomputations[1][1])

for i in range(MAX_BLINKS):
    stones = blink(stones)

print('Final number of stones:', len(stones))
