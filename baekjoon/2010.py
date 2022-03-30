import sys
input = sys.stdin.readline

repeat = int(input())
cnt = 0
for i in range(repeat):
  cnt += int(input()) - 1

print(cnt + 1)