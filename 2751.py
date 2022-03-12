import sys
repeat = int(sys.stdin.readline())
arr = []

for i in range(repeat):
  arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
  print(i)

# input() 함수 사용 시 시간초과 출력