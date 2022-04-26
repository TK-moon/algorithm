l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
  for i, n in enumerate(l): # 미리 생성해둔 배열의 인덱스와 값들로 반복
    # 만약 반복문의 값이 문자열에 들어있으면, 그 문자열을 반복문의 인덱스 변호로 치환
    if n in s:
      s = s.replace(n, str(i))
      
  return int(s)