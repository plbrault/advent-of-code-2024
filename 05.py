from functools import cmp_to_key

class OrderingRule:
  is_before: [int]
  is_after: [int]
  def __init__(self):
    self.is_before = []
    self.is_after = []

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

def compare_page_numbers(x, y):
  if x in ordering_rules[y].is_before:
    return -1
  if y in ordering_rules[x].is_before:
    return 1
  return 0

correct_updates = []

for page_update in page_updates:
  ordered_update = sorted(page_update, key=cmp_to_key(compare_page_numbers))
  if ordered_update[0] == page_update[0]:
    print(ordered_update, '!!!!!!!!!!!!!!', page_update)
  #if ordered_update == page_update:
    #correct_updates.append(page_update)

print('Correct updates:', correct_updates)
