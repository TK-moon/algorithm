import sys
input = sys.stdin.readline
repeat = int(input())

words = []

for i in range(repeat):
  words.append(input().strip())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for i in words:
  print(i)