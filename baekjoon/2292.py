room_number = int(input()) - 1

level = 1
step = 6

while room_number > 0:
	level += 1
	room_number -= step
	step += 6

print(level)



# level 1
# room number 13
# step 6

# level 2
# room number 7
# step 12

# level 3
# room number -5
# step 18

# print 3




# 1 = 1
# : 1

# 2 = 2
# 3 = 2
# 4 = 2
# 5 = 2
# 6 = 2
# 7 = 2
# : 6

# 8 = 3
# 9 = 3
# 10 = 3
# 11 = 3
# 12 = 3
# 13 = 3
# 14 = 3
# 15 = 3
# 16 = 3
# 17 = 3
# 18 = 3
# 19 = 3
# : 12

# 20 = 4
# 21 = 4
# ...
# 37 = 4
# : 18