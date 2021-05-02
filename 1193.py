number = int(input())

line = 0

# 수학 개싫네 진짜
while line < number:
	number = number - line
	line += 1

if line & 1:
	a = line - number + 1
	b = number
else:
	a = number
	b = line - number + 1

print('%d/%d' %(a, b))