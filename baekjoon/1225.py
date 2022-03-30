# 시간초과
# a, b = input().split()
# arr = []
# for i in a:
#   for j in b:
#     arr.append(int(i) * int(j))

# print(sum(arr))

# 정답코드
a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))
print(sum(a) * sum(b))