GUARD_UP = '^'
GUARD_DOWN = 'v'
GUARD_LEFT = '<'
GUARD_RIGHT = '>'
OBSTACLE = '#'
VISITED_POINT = 'X'

class Map():
  def __init__(self):
    with open('input.txt', 'r') as file:
      self._map = [list(line.strip()) for line in file]

    for y in range(len(self._map)):
      for x in range(len(self._map[y])):
        if self._map[y][x] in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
          self._guard_pos = (x, y)
          break

  def check_if_pos_on_map(self, x, y):
    return 0 <= y < len(self._map) and 0 <= x < len(self._map[y])

  @property
  def guard_pos(self):
    return self._guard_pos

  @property
  def guard_x(self):
    return self._guard_pos[0]

  @property
  def guard_y(self):
    return self._guard_pos[1]

  @property
  def guard_symbol(self):
    return self._map[self.guard_y][self.guard_x]

  @guard.setter
  def guard_symbol(self, value):
    self._map[self.guard_y][self.guard_x] = value

  @property
  def guard_still_on_map(self):
    return self.check_if_pos_on_map(self.guard_x, self.guard_y)

  @property
  def guard_next_pos(self):
    if self.guard_symbol == GUARD_UP:
      return (self.guard_x, self.guard_y - 1)
    if self.guard_symbol == GUARD_LEFT:
      return (self.guard_x - 1, self.guard_y)
    if self.guard_symbol == GUARD_DOWN:
      return (self.guard_x, self.guard_y + 1)
    if self.guard_symbol == GUARD_RIGHT:
      return (self.guard_x + 1, self.guard_y)

  @property
  def guard_can_move(self):
    if not self.check_if_pos_on_map(*self.guard_next_pos):
      return True
    next_x, next_y = self.guard_next_pos
    return self._map[next_y][next_x] != OBSTACLE

  def turn_guard(self):
    if self.guard_symbol == GUARD_UP:
      self.guard_symbol = GUARD_RIGHT
    elif self.guard_symbol == GUARD_RIGHT:
      self.guard_symbol = GUARD_DOWN
    elif self.guard_symbol == GUARD_DOWN:
      self.guard_symbol = GUARD_LEFT
    elif self.guard_symbol == GUARD_LEFT:
      self.guard_symbol = GUARD_UP

  def move_guard(self):
    if self.guard_can_move:
      next_x, next_y = self.guard_next_pos
      previous_guard_symbol = self.guard_symbol
      self.guard_symbol = VISITED_POINT
      self._guard_pos = (next_x, next_y)
      if self.guard_still_on_map:
        self.guard_symbol = previous_guard_symbol
    else:
      self.turn_guard()
      self.move_guard()



  
