from dataclasses import dataclass

@dataclass
class Location:
  frequency: str = None
  is_antinode: bool = False
  position: tuple = (-1, -1)

map = []

with open('input.txt', 'r') as file:
  for y, line in enumerate(file):
    map_row = []
    for x, char in enumerate(line):
      location = Location()
      if char != '.':
        location.frequency = char
      location.position = (x, y)
      map_row.append(location)
    map.append(map_row)

antennas = []
for row in map:
  for location in row:
    if location.frequency is not None:
      antennas.append(location)

antinodes = []

def get_line_equation(location1, location2):
  x1, y1 = location1.position
  x2, y2 = location2.position  
  if x1 == x2:
    return None
  m = (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  return m, b

def is_on_map(x, y):
  return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)

for antenna in antennas:
  for other_antenna in antennas:
    if (
      antenna.position != other_antenna.position
      and antenna.frequency == other_antenna.frequency
    ):
      line_equation = get_line_equation(antenna, other_antenna)
      if line_equation is None: # The antennas have the same X position
        [y1, y2] = sorted([antenna.position[1], other_antenna.position[1]])
        antinode1_y = y1 - abs(y2 - y1)
        antinode2_y = y2 + abs(y2 - y1)
        if is_on_map(antenna.position[0], antinode1_y):
          map[antinode1_y][antenna.position[0]].is_antinode = True
        if is_on_map(antenna.position[0], antinode2_y):
          map[antinode2_y][antenna.position[0]].is_antinode = True

antinode_count = len([location for row in map for location in row if location.is_antinode])

print('Number of antinodes:', antinode_count)
