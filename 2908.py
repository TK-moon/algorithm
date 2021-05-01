a, b = input().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()

a = int(''.join(a))
b = int(''.join(b))

print(max([a, b]))