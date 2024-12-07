GUARD_UP = '^'
GUARD_DOWN = 'v'
GUARD_LEFT = '<'
GUARD_RIGHT = '>'
OBSTACLE = '#' 

class Map():
  @property
  def guard_pos(self):
    return self._guard_pos

  def __init__(self):
    with open('input.txt', 'r') as file:
      self._map = [list(line.strip()) for line in file]

    for y in range(len(self._map)):
      for x in range(len(self._map[y])):
        if self._map[y][x] in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
          self._guard_pos = (x, y)
          break

map = Map()
print(map.guard_pos)

  
