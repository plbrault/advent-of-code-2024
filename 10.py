map: [[int]] = []

with open('input.txt', 'r') as file:
    for line in file:
        map_row = []
        for char in line.strip():
            map_row.append(int(char))
        map.append(map_row)

def walk_trail(x: int, y: int, end_positions: set[tuple[int, int]]) -> int:
    height = map[y][x]
    if height == 9:
        end_positions.add((x, y))
        return

    # left
    if x > 0 and map[y][x - 1] == height + 1:
        walk_trail(x - 1, y, end_positions)
    # up
    if y > 0 and map[y - 1][x] == height + 1:
        walk_trail(x, y - 1, end_positions)
    # right
    if x < len(map[y]) - 1 and map[y][x + 1] == height + 1:
        walk_trail(x + 1, y, end_positions)
    # down
    if y < len(map) - 1 and map[y + 1][x] == height + 1:
        walk_trail(x, y + 1, end_positions)

total_score = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 0:
            end_positions = set()
            walk_trail(x, y, end_positions)
            total_score += len(end_positions)

print('Sum of scores for all trailheads:', total_score)
