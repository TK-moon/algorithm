# xList = []
# yList = []

# for i in range(3):
# 	x, y = map(int, input().split())
# 	xList.append(x)
# 	yList.append(y)

# seenX = set()
# dupX = 0
# for num in xList:
# 	if num in seenX:
# 		dupX = num
# 		break
# 	else: seenX.add(num)

# seenY = set()
# dupY = 0
# for num in yList:
# 	if num in seenY:
# 		dupY = num
# 		break
# 	else: seenY.add(num)

# for num in xList:
# 	if num != dupX:
# 		x = num
# for num in yList:
# 	if num != dupY:
# 		y = num

# print(x, y)


xList = []
yList = []

for i in range(3):
	x, y = map(int, input().split())
	
	if x in xList: xList.remove(x)
	else: xList.append(x)

	if y in yList: yList.remove(y)
	else: yList.append(y)

print(xList[0], yList[0])