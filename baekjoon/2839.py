kg = int(input())

count = 0

while kg >= 0:
	if kg % 5 == 0:
		count += kg // 5
		print(count)
		break
	else:
		kg -= 3
		count += 1
else:
	print(-1)