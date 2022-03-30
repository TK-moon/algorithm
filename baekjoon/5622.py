dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = input()

number_list = list()

for i in range(0, len(s)):
	for j in dial:
		if s[i] in j:
			number_list.append(dial.index(j) + 3)

print(sum(number_list))