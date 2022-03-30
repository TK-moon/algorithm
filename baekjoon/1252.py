a, b = input().split()
a = int('0b' + a, 2)
b = int('0b' + b, 2)
print(format(a + b, 'b'))