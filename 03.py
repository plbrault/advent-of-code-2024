import re

program_content = ''

with open('input.txt', 'r') as file:
  program_content = file.read()

multiply_pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(multiply_pattern, program_content)

sum = 0
for match in matches:
  numbers = re.findall(r'\d{1,3}', match)
  sum += int(numbers[0]) * int(numbers[1])

print("Sum of all multiplications:", sum)
