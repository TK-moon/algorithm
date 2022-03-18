import sys
input = sys.stdin.readline

money, peoples = map(int, input().strip().split())

print(money // peoples)
print(money % peoples)