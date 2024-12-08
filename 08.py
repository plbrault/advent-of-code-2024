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
