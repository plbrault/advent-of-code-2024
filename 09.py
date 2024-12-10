numbers: list[int]

with open('input.txt', 'r') as file:
    first_line = file.readline().strip()
    numbers = [int(number) for number in first_line]
