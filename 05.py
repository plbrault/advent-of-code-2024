class OrderingRule:
  is_before: [int] = []
  is_after: [int] = []

raw_ordering_rules = []
page_updates = []

with open('input.txt', 'r') as file:
  line = file.readline()
  position = file.tell()
  while line.strip() != '':
    raw_ordering_rules.append([
      int(element) for element in line.split('|')
    ])
    line = file.readline()
    position = file.tell()
  file.seek(position)
  for line in file:
    page_updates.append([
      int(element) for element in line.split(',')
    ])

ordering_rules = {}

for raw_ordering_rule in raw_ordering_rules:
  [first_number, second_number] = raw_ordering_rule
  if first_number not in ordering_rules:
    ordering_rules[first_number] = OrderingRule()
  if second_number not in ordering_rules:
    ordering_rules[second_number] = OrderingRule()
  ordering_rules[first_number].is_before.append(second_number)
  ordering_rules[second_number].is_after.append(first_number)

for rule in ordering_rules:
  print('IS BEFORE', rule, ordering_rules[rule].is_before)
  print('IS AFTER', rule, ordering_rules[rule].is_after)
  print('-------------------------------------------------')
