repeat = int(input())

for _ in range(repeat):
  string, clip = map(str, input().split())
  paste = string.count(clip)
  string = string.replace(clip, '')
  print(len(string) + paste)