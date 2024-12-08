from dataclasses import dataclass

@dataclass
class Location:
  frequency: str = None
  is_antinode: bool = False

map = []

with open('input.txt', 'r') as file:
  for line in file:
    map_row = []
    for char in line:
      location = Location()
      if char != '.':
        location.frequency = char
      map_row.append(location)
    map.append(map_row)

print(map)
