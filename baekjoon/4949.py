paragraph = []

open_brackets = ['(', '{', '[']
close_backets = [')', '}', ']']

while True:
  line = input()
  if line == '.': break
  paragraph.append(line)

for line in paragraph:
  stack = []
  validation = True
  for alphabet in line:

    if alphabet in open_brackets: # 문자가 여는 괄호인 경우
      stack.append(alphabet)
    
    elif alphabet in close_backets: #문자가 닫는 괄호인 경우
      if not stack: # 스택이 비어있으면 Validation Falase
        # validation = False
        stack.append(alphabet)
        break
      
      else:
        last_open_bracket = stack[-1] # 마지막 연 괄호
        index = open_brackets.index(last_open_bracket) # 마지막 연 괄호의 인덱스
        expect_close_bracket = close_backets[index] # 기대하는 닫는 괄호

        if expect_close_bracket == alphabet: # 닫는 괄호가 현재 알파벳과 짝이 맞으면
          stack.pop()
        else: # 짝이 맞지 않으면
          # validation = False
          stack.append(alphabet)
          break
      
  print('yes' if not stack else 'no')

  # 왜 validation 변수 플래그로 처리하면 틀렸다고 나오지?