a = []
b = []

a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

b.append(int(input()))
b.append(int(input()))

a.sort(reverse=True)
b.sort(reverse=True)

print(sum(a[0: 3]) + b[0])