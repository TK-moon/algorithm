n = int(input())

count = 0

for i in range(0, n):
	word = input()
	s = sorted(word, key=word.find)
	word = list(word)
	if word == s: count += 1

print(count)