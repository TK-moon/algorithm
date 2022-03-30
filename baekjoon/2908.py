# a, b = input().split()

# a = list(a)
# b = list(b)

# a.reverse()
# b.reverse()

# a = int(''.join(a))
# b = int(''.join(b))

# print(max([a, b]))

a, b = input().split()

a = int(''.join(list(reversed(list(a)))))
b = int(''.join(list(reversed(list(b)))))

print(max([a, b]))