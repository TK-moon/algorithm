repeat = int(input())

for _ in range(repeat):
  input()
  list1 = list(input().split())
  list2 = list(input().split())
  list1.sort()
  list2.sort()
  print('NOT CHEATER' if list1 == list2 else 'CHEATER')