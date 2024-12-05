def check_for_xmas(puzzle, row, col):
  # Horizontal backwards
  if col > 2:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row][col-1] == 'M'
      and puzzle[row][col-2] == 'A'
      and puzzle[row][col-3] == 'S'
    ):
      return True
  # Vertical upwards
  if row > 2:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row-1][col] == 'M'
      and puzzle[row-2][col] == 'A'
      and puzzle[row-3][col] == 'S'
    ):
      return True
  # Horizontal forwards
  if len(puzzle[row]) - col > 3:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row][col+1] == 'M'
      and puzzle[row][col+2] == 'A'
      and puzzle[row][col+3] == 'S'
    ):
      return True
  # Vertical downwards
  if len(puzzle) - row > 3:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row+1][col] == 'M'
      and puzzle[row+2][col] == 'A'
      and puzzle[row+3][col] == 'S'
    ):
      return True
  # Diagonal upwards left
  if row > 2 and col > 2:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row-1][col-1] == 'M'
      and puzzle[row-2][col-2] == 'A'
      and puzzle[row-3][col-3] == 'S'
    ):
      return True
  # Diagonal upwards right
  if row > 2 and len(puzzle[row]) - col > 3:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row-1][col+1] == 'M'
      and puzzle[row-2][col+2] == 'A'
      and puzzle[row-3][col+3] == 'S'
    ):
      return True
  # Diagonal downwards left
  if len(puzzle) - row > 3 and col > 2:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row+1][col-1] == 'M'
      and puzzle[row+2][col-2] == 'A'
      and puzzle[row+3][col-3] == 'S'
    ):
      return True
  # Diagonal downwards right
  if len(puzzle) - row > 3 and len(puzzle[row]) - col > 3:
    if (
      puzzle[row][col] == 'X'
      and puzzle[row+1][col+1] == 'M'
      and puzzle[row+2][col+2] == 'A'
      and puzzle[row+3][col+3] == 'S'
    ):
      return True
  return False

puzzle = []

with open('input.txt', 'r') as file:
  for line in file:
    puzzle.append(list(line.strip()))

xmas_count = 0

for row in range(len(puzzle)):
  for col in range(len(puzzle[row])):
    if check_for_xmas(puzzle, row, col):
      xmas_count += 1

print('Number of XMAS occurrences:', xmas_count)
