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



# 인터넷 풀이 2
## set을 활용

# temp=input().split(" ") # 값을 받아옴(문자열)
# list=[]
# for i in temp:
#     list.append(int(i)) # 정수형으로 바꿔서 list라는 배열에 넣음
# list.sort() # 리스트 정렬
# list_s = set(list) # 리스트를 집합화 시켜주고 list_s에 넣어줌

# if len(list_s)==1 : # 모두 같은눈이 나왔을 때
#     print(10000+list[0]*100)
# elif len(list_s)==3 : # 모두 다른눈이 나왔을 때
#     print(list[-1]*100)
# else : # 2개가 같은눈이 나왔을 때
#     print(1000+list[1]*100)  # 총 3개의 원소 중 정렬을 했을 때 중간이 같은수