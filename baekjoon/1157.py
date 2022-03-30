s = input().upper()

arr = list()

for i in range(65, 91):
	count = 0
	for j in list(s):
		if j == chr(i): count += 1
	arr.append(count)

if arr.count(max(arr)) == 1: print(chr(65 + arr.index(max(arr))))
else: print('?')