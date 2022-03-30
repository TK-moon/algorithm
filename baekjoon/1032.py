import sys
input = sys.stdin.readline

repeat = int(input())

lines = []

for i in range(repeat):
  lines.append(input().strip())

word_length = len(lines[0])

computed_query = []

for word_index in range(word_length):
  line = []
  for line_index in range(repeat):
    line.append(lines[0][word_index] == lines[line_index][word_index])

  if all(line): computed_query.append(lines[0][word_index])
  else: computed_query.append('?')

print(''.join(computed_query))