import re

program_content = ''
with open('input.txt', 'r') as file:
  program_content = file.read()

program_parts_between_do_instructions = program_content.split('do()')

multiply_pattern = r'mul\(\d{1,3},\d{1,3}\)'
sum = 0

for part in program_parts_between_do_instructions:
  enabled_program_part = part.split('don\'t()')[0]
  matches = re.findall(multiply_pattern, enabled_program_part)
  for match in matches:
    numbers = re.findall(r'\d{1,3}', match)
    sum += int(numbers[0]) * int(numbers[1])

print("Sum of all enabled multiplications:", sum)
