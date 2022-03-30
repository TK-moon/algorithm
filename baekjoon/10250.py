repeat = int(input())

for i in range(repeat):
	height, width, n = map(int, input().split())
	
	floor_number = n % height
	room_number = n // height + 1

	if floor_number == 0:
		floor_number = height
		room_number = room_number - 1
	
	print(floor_number * 100 + room_number)