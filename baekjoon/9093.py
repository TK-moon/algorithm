# 직접 푼 소스코드

# n = int(input())
# for _ in range(n):
#   words = input().split()
#   result = []
#   for word in words:
#     result.append(''.join(list(reversed(list(word)))))

#   print(*result)


# 인터넷 참고
## ::-1 해주면 거꾸로 출력 가능
n = int(input())
for i in range(n):
  string = input().split()
  for j in string:
    print(j[::-1], end=' ')