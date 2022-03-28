import collections
repeat = int(input())
names = []
for _ in range(repeat):
  names.append(input()[0])

countes = collections.Counter(names)
arr = []
for i in countes:
  if countes[i] >= 5:
    arr.append(i)

arr.sort()
print(''.join(arr) if len(arr) else 'PREDAJA')