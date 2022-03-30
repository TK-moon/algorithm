import collections
lines = []
while True:
  line = input()
  if (line == '#'): break
  lines.append(map(lambda x: x.lower(), line))

for line in lines:
  count = collections.Counter(line)
  print(count['a'] + count['e'] + count['i'] + count['o'] + count['u'])