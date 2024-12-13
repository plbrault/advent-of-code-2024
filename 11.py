stones : [int]

with open('input.txt') as file:
    line = file.readline()
    stones = [int(number) for number in line.split(' ')]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                new_stones.append(int(stone_str[:len(stone_str)//2]))
                new_stones.append(int(stone_str[len(stone_str)//2:]))
            else:
                new_stones.append(stone * 2024)
    return new_stones

for i in range(25):
    stones = blink(stones)

print('Number of stones after 25 blinks:', len(stones))
