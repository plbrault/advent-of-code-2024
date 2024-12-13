stones : [int]

with open('input.txt') as file:
    line = file.readline()
    stones = [int(number) for number in line.split(' ')]

print(stones)
