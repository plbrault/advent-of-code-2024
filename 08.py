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
    for x, char in enumerate(line.strip()):
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
      antinode1_x = antinode1_y = antinode2_x = antinode2_y = None
      if line_equation is None: # The antennas have the same X position
        antinode1_x = antinode2_x = antenna.position[0]
        [y1, y2] = sorted([antenna.position[1], other_antenna.position[1]])
        y_diff = y2 - y1
        antinode1_y = y1 - y_diff
        antinode2_y = y2 + y_diff
      else:
        [x1, x2] = sorted([antenna.position[0], other_antenna.position[0]])
        x_diff = x2 - x1
        antinode1_x = x1 - x_diff
        antinode2_x = x2 + x_diff
        m, b = line_equation
        antinode1_y = m * antinode1_x + b
        antinode2_y = m * antinode2_x + b
      if antinode1_y.is_integer() and is_on_map(antinode1_x, antinode1_y):
        map[int(antinode1_y)][antinode1_x].is_antinode = True
      if antinode2_y.is_integer() and is_on_map(antinode2_x, antinode2_y):
        map[int(antinode2_y)][antinode2_x].is_antinode = True

antinode_count = len([location for row in map for location in row if location.is_antinode])

print('Number of antinodes:', antinode_count)
