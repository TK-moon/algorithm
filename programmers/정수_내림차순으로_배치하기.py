def solution(n):
  l = list(str(int(n)))
  l.sort(reverse=True)
  return int("".join(l))

# n은 자연수라고 나와있는데, n int로 형변환을 해줘야 컴파일 에러가 나지 않는다.