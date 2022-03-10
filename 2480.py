arr = list(map(int, input().split()))

# print(list(2 == arr.count(n) for n in arr))

if (all(arr[0] == item for item in arr)):
  print(10000 + arr[0] * 1000)

elif (2 in [arr.count(n) for n in arr]):
  for i in arr:
    if arr.count(i) == 2:
      print(1000 + i * 100)
      break

else:
  print(max(arr) * 100)


# 인터넷 풀이 1
## 단순하게 풀이 : 위에 작성한 for 문 돌리는것보다 연산이 적다.

# a, b, c = map(int, input().split())

# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))