s = input()

a = s.split('1')
b = s.split('0')

a = len([x for x in a if x])
b = len([x for x in b if x])

print(min(a, b))