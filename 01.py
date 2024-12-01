list1 = []
list2 = []

with open('input.txt', 'r') as input_file:
  for line in input_file:
    parts = line.split()
    list1.append(int(parts[0]))
    list2.append(int(parts[1]))

list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
  distance += abs(list1[i] - list2[i])

print('Distance:', distance)

similarity_score = 0
for element in list1:
  count = list2.count(element)
  similarity_score += count * element

print('Similarity score:', similarity_score)
