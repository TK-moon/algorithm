def solution(n):
  n_binary = bin(n)[2:]
  n_one_count = n_binary.count('1')
  
  i = n + 1
  while True:
    binary = bin(i)[2:]
    count = binary.count('1')
    if count == n_one_count:
      return int(binary, 2)
    i += 1


# 코드 간소화
def solution(n):
  ncount = bin(n).count('1')

  while True:
    n = n + 1
    if ncount == bin(n).count('1'):
      return n
    