def solution(record):
  idtable = {}
  for i in record:
    command = i.split()
    if command[0] != 'Leave':
      idtable[command[1]] = command[2]
  
  result = []
  for i in record:
    command = i.split()
    if command[0] == 'Enter':
      result.append('{0}님이 들어왔습니다.'.format(idtable[command[1]]))
    elif command[0] == 'Leave':
      result.append('{0}님이 나갔습니다.'.format(idtable[command[1]]))
          
  return result

# 하나의 for문으로 시도하지 말기
# for문 두개로 나눠 풀어도 시간복잡도 O(n) 이라 괜찮다.