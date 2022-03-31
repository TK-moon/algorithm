from bisect import bisect_left, bisect_right

def counter(lst, target):
  left = bisect_left(lst, target) # 왼쪽에서부터 탐색하여 인덱스 반환
  right = bisect_right(lst, target) # 오른쪽부터 탐색하여 인덱스 반환
  return right - left # 두 인덱스의 차이를 반환하면 그 사이에 몇개가 들어있는지 알 수 있다.

n1 = int(input())
l1 = list(map(int, input().split()))
l1.sort()

n2 = int(input())
l2 = list(map(int, input().split()))

for i in l2:
  count = counter(l1, i)
  print(count, end=' ')
