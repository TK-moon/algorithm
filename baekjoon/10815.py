n1 = int(input())
l1 = list(map(int, input().split()))
l1.sort()

n2 = int(input())
l2 = list(map(int, input().split()))

def bin_search(l, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if l[mid] == target: return True
    if l[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return False


for i in l2:
  result = bin_search(l1, i, 0, n1 - 1)
  print(1 if result else 0, end=" ")