a, b = map(bool, map(int, input().split()))
print(True if not (a ^ b) else False)