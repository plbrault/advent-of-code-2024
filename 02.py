def is_increasing(report):
  for i in range(len(report) - 1):
    if report[i] >= report[i + 1]:
      return False
  return True

def is_decreasing(report):
  for i in range(len(report) - 1):
    if report[i] <= report[i + 1]:
      return False
  return True

def is_gradual(report):
  for i in range(len(report) - 1):
    if abs(report[i] - report[i + 1]) > 3:
      return False
  return True

def is_safe(report):
  return (is_increasing(report) or is_decreasing(report)) and is_gradual(report)

def is_safe_with_removed_level(report):
  for i in range(len(report)):
    if is_safe(report[:i] + report[i + 1:]):
      return True
  return False

reports = []
safe_reports_count = 0

with open('input.txt', 'r') as input_file:
  for line in input_file:
    levels = [int(part) for part in line.split()]
    reports.append(levels)

safe_reports_count = len([
  report for report in reports
    if is_safe(report) or is_safe_with_removed_level(report)
])

print('Safe reports count:', safe_reports_count)
