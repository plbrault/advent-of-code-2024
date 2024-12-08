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

print(get_possible_results([81, 40, 27]))
  
