import sys
input = sys.stdin.readline

input()
numbers = list(map(int, input().strip().split()))
numbers.sort()

print(numbers[-1] * numbers[0])