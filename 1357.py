a, b = map(list, input().split())

a.reverse()
b.reverse()

a = int(''.join(a))
b = int(''.join(b))

arr = list(str(a + b))
arr.reverse()
print(int(''.join(arr)))