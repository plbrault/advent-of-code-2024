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

operators = ['+', '*']

def get_possible_results(operands):
  if len(operands) == 1:
    return operands
  else:
    results = []
    for operator in operators:
      results += [
        eval(str(operands[-1]) + operator + str(result))
          for result in get_possible_results(operands[:-1])
      ]
    return results

total_calibration_result = 0

start_time = datetime.now()
for equation in equations:
  possible_results = get_possible_results(equation.operands)
  if equation.test_value in possible_results:
    total_calibration_result += equation.test_value
end_time = datetime.now()    

print('Total calibration result:', total_calibration_result)
print('Executed in:', (end_time - start_time).total_seconds(), 'seconds.')
