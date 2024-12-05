def check_for_xmas(puzzle, row, col):
  if puzzle[row][col] != 'X':
    return False
  num_occurrences = 0
  # Horizontal backwards
  if col > 2:
    if (
      puzzle[row][col-1] == 'M'
      and puzzle[row][col-2] == 'A'
      and puzzle[row][col-3] == 'S'
    ):
      num_occurrences += 1
  # Vertical upwards
  if row > 2:
    if (
      puzzle[row-1][col] == 'M'
      and puzzle[row-2][col] == 'A'
      and puzzle[row-3][col] == 'S'
    ):
      num_occurrences += 1
  # Horizontal forwards
  if len(puzzle[row]) - col > 3:
    if (
      puzzle[row][col+1] == 'M'
      and puzzle[row][col+2] == 'A'
      and puzzle[row][col+3] == 'S'
    ):
      num_occurrences += 1
  # Vertical downwards
  if len(puzzle) - row > 3:
    if (
      puzzle[row+1][col] == 'M'
      and puzzle[row+2][col] == 'A'
      and puzzle[row+3][col] == 'S'
    ):
      num_occurrences += 1
  # Diagonal upwards left
  if row > 2 and col > 2:
    if (
      puzzle[row-1][col-1] == 'M'
      and puzzle[row-2][col-2] == 'A'
      and puzzle[row-3][col-3] == 'S'
    ):
      num_occurrences += 1
  # Diagonal upwards right
  if row > 2 and len(puzzle[row]) - col > 3:
    if (
      puzzle[row-1][col+1] == 'M'
      and puzzle[row-2][col+2] == 'A'
      and puzzle[row-3][col+3] == 'S'
    ):
      num_occurrences += 1
  # Diagonal downwards left
  if len(puzzle) - row > 3 and col > 2:
    if (
      puzzle[row+1][col-1] == 'M'
      and puzzle[row+2][col-2] == 'A'
      and puzzle[row+3][col-3] == 'S'
    ):
      num_occurrences += 1
  # Diagonal downwards right
  if len(puzzle) - row > 3 and len(puzzle[row]) - col > 3:
    if (
      puzzle[row+1][col+1] == 'M'
      and puzzle[row+2][col+2] == 'A'
      and puzzle[row+3][col+3] == 'S'
    ):
      num_occurrences += 1
  return num_occurrences

def check_for_x_mas(puzzle, row, col):
  if puzzle[row][col] != 'A':
    return False
  if row < 1 or col < 1 or row > len(puzzle) - 2 or col > len(puzzle[row]) - 2:
    return False
  if (
    (
      (puzzle[row-1][col-1] == 'M' and puzzle[row+1][col+1] == 'S')
      or (puzzle[row-1][col-1] == 'S' and puzzle[row+1][col+1] == 'M')
    )
    and
    (
      (puzzle[row-1][col+1] == 'M' and puzzle[row+1][col-1] == 'S')
      or (puzzle[row-1][col+1] == 'S' and puzzle[row+1][col-1] == 'M')
    )
  ):
    return True
  return False

puzzle = []

with open('input.txt', 'r') as file:
  for line in file:
    puzzle.append(list(line.strip()))

# Part 1
xmas_count = 0
for row in range(len(puzzle)):
  for col in range(len(puzzle[row])):
    xmas_count += check_for_xmas(puzzle, row, col)
print('Number of XMAS occurrences:', xmas_count)

# Part 2
x_mas_count = 0
for row in range(len(puzzle)):
  for col in range(len(puzzle[row])):
    x_mas_count += int(check_for_x_mas(puzzle, row, col))
print ('Number of X-MAS occurrences:', x_mas_count)
