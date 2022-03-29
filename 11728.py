import sys
input = sys.stdin.readline
input()
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))

l = b + c
l.sort()
print(*l)