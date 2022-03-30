user_input = input().split()

h = int(user_input[0])
m = int(user_input[1])

if (m < 45):
	m = 60 + m - 45
	h -= 1
	if (h < 0):
		h = 23
else:
	m -= 45

print(h, m)