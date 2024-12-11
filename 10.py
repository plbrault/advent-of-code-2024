map: [[int]] = []

with open('input.txt', 'r') as file:
    for line in file:
        map_row = []
        for char in line.strip():
            map_row.append(int(char))
        map.append(map_row)
