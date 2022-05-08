length = int(input())
string = input()

number_buffer = ''

for i in range(length):
  char = string[i]
  if '0' <= char and char <= '9': number_buffer += char
  else: number_buffer += ' '

print(sum(map(int, number_buffer.split())))