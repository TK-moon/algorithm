# 메모리 초과 코드

# import sys
# repeat = int(sys.stdin.readline())
# arr = []
# for i in range(repeat):
#   arr.append(int(sys.stdin.readline()))
# arr.sort()
# for i in arr:
#   print(i)

# 그냥 메모리가 많이 박혀있는 컴퓨터를 쓰는게 코드 가독성이 더 좋다.



# 메모리 안초과 코드
# 실무에서 이렇게 코드짜면 욕먹는다
import sys
repeat = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(repeat):
  arr[int(sys.stdin.readline())] += 1
# arr의 인덱스가 출력될 숫자이고, 그 숫자를 출력할 카운트를 올려준다.

for i in range(10001):
  if arr[i] != 0:
    for j in range(arr[i]):
      print(i)