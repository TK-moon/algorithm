import itertools
n = int(input())

input_arr = []
max_arr = []

for i in range(n):
  input_arr.append(list(map(int, input().split())))

for i in input_arr:
  max_arr.append(max(list(map(lambda x: int(str(sum(x))[-1]), list(itertools.combinations(i, 3))))))

max_data = 0
for i in max_arr:
  if max_data < i: max_data = i

idx_arr = []
for index, data in enumerate(max_arr):
  if data == max_data:
    idx_arr.append(index)

print(idx_arr[-1] + 1)