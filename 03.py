import re

program_content = ''

with open('input.txt', 'r') as file:
  program_content = file.read()

multiply_pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(multiply_pattern, program_content)

print(matches)
