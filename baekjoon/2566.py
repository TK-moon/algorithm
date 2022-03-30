
max_num = 0
max_x = 0
max_y = 0
for i in range(9):
  line = list(map(int, input().split()))
  line_max = max(line)
  if (max_num < line_max): 
    max_num = line_max
    max_x = line.index(line_max) + 1
    max_y = i + 1

print(max_num)
print(max_y, max_x)
   