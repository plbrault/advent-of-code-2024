ordering_rules = []
page_updates = []

with open('input.txt', 'r') as file:
  line = file.readline()
  position = file.tell()
  while line.strip() != '':
    ordering_rules.append([
      int(element) for element in line.split('|')
    ])
    line = file.readline()
    position = file.tell()
  file.seek(position)
  for line in file:
    page_updates.append([
      int(element) for element in line.split(',')
    ])

print(page_updates)

    