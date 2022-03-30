a, b = map(bool, map(int, input().split()))
print(True if (not a and b) or (not b and a) else False)