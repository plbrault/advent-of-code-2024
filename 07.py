from datetime import datetime

class Equation:
  def __init__(self, test_value: int, operands: list[int]):
    self.test_value = test_value
    self.operands = operands

  def __repr__(self):
    return f'{self.test_value} : {self.operands}'

equations = []

with open('input.txt', 'r') as file:
  for line in file:
    colon_split = line.split(':')
    test_value = int(colon_split[0])
    operands = list(map(int, colon_split[1].split()))
    equations.append(Equation(test_value, operands))

operators = ['+', '*', '']

def get_possible_results(left_operands: [int], right_operands: [int], max_result: [int]):
  if len(left_operands) < 2:
    if len(right_operands) == 0:
      return left_operands
    return get_possible_results(left_operands + [right_operands[0]], right_operands[1:], max_result)
  if left_operands[0] > max_result:
    return [left_operands[0]]
  possible_results = []
  for operator in operators:
    left_result = eval(f'{left_operands[0]}{operator}{left_operands[1]}')
    possible_results += get_possible_results([left_result], right_operands, max_result)
  return possible_results

total_calibration_result = 0

start_time = datetime.now()
for equation in equations:
  possible_results = get_possible_results([], equation.operands, equation.test_value)
  if equation.test_value in possible_results:
    total_calibration_result += equation.test_value
end_time = datetime.now()    

print('Total calibration result:', total_calibration_result)
print('Executed in:', (end_time - start_time).total_seconds(), 'seconds.')
