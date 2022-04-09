def solution(numbers):
  s = list(map(str, numbers))
  s.sort(key=lambda x: x * 3, reverse=True)
  
  
  # 왜 * 3을 하는지 모르겠다. -> 
  # 문자열 정렬은
  # 1. 0번 인덱스끼리 아스키로 치환하여 비교
  # 2. 0번 인덱스가 같으면 1번 인덱스를 아스키로 치환하여 비교
  
  
  return str(int(''.join(s)))