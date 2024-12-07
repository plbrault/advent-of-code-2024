GUARD_UP = '^'
GUARD_DOWN = 'v'
GUARD_LEFT = '<'
GUARD_RIGHT = '>'
OBSTACLE = '#'
VISITED_POINT = 'X'
UNVISITED_POINT = '.'

class Map():
  def __init__(self):
    with open('input.txt', 'r') as file:
      self._map = [list(line.strip()) for line in file]

    for y in range(len(self._map)):
      for x in range(len(self._map[y])):
        if self._map[y][x] in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
          self._initial_guard_pos = self._guard_pos = (x, y)
          self._initial_guard_symbol = self._map[y][x]
          break

    self._obstacle_hits = []
    self._loop_detected = False

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

  @guard_symbol.setter
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
      return self.check_if_pos_on_map(*self.guard_pos)
    next_x, next_y = self.guard_next_pos
    return self._map[next_y][next_x] != OBSTACLE

  @property
  def loop_detected(self):
    return self._loop_detected

  @loop_detected.setter
  def loop_detected(self, value):
    self._loop_detected = value

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
      obstacle_hit = (self.guard_next_pos, self.guard_symbol)
      if obstacle_hit in self._obstacle_hits:
        self._loop_detected = True
      else:
        self._obstacle_hits.append(obstacle_hit)
      self.turn_guard()
      self.move_guard()

  def get_visited_positions(self):
    positions = []
    for y in range(len(self._map)):
      for x in range(len(self._map[y])):
        if self._map[y][x] == VISITED_POINT:
          positions.append((x, y))
    return positions

  def count_visited_positions(self):
    return len(self.get_visited_positions())

  def add_obstacle(self, x, y):
    self._map[y][x] = OBSTACLE

  def remove_obstacle(self, x, y):
    if (x, y) in [hit[0] for hit in self._obstacle_hits]:
      self._map[y][x] = VISITED_POINT
    else:
      self._map[y][x] = UNVISITED_POINT

  def reset_guard_pos(self):
    old_guard_pos = self._guard_pos
    self._guard_pos = self._initial_guard_pos
    if self.check_if_pos_on_map(*old_guard_pos):
      self._map[old_guard_pos[1]][old_guard_pos[0]] = VISITED_POINT
    self.guard_symbol = self._initial_guard_symbol

map = Map()

while map.guard_still_on_map:
  map.move_guard()

print('Number of distinct visited positions:', map.count_visited_positions())

visited_positions = map.get_visited_positions()

loop_detections = 0

for position in visited_positions:
  map.reset_guard_pos()
  if position != map.guard_pos:
    map.add_obstacle(*position)
    while map.guard_still_on_map and not map.loop_detected:
      map.move_guard()
    if map.loop_detected:
      loop_detections += 1
      map.loop_detected = False
    map.remove_obstacle(*position)

print('Number of loop detections:', loop_detections)
