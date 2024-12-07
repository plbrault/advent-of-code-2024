GUARD_UP = '^'
GUARD_DOWN = 'v'
GUARD_LEFT = '<'
GUARD_RIGHT = '>'
OBSTACLE = '#' 

map = None
guard_position = None

with open('input.txt', 'r') as file:
  map = [list(line.strip()) for line in file]

for row in range(len(map)):
  for col in range(len(map[row])):
    if map[row][col] in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
      guard_position = (row, col)
      break

print('Initial guard position:', guard_position)
