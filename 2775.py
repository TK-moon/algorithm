import sys
input = sys.stdin.readline

repeat = int(input())

building = []

for loop in range(repeat):
  floor = int(input())
  unit = int(input())

  # 미리 0층의 각 호에 살고있는 사람들의 수를 추가
  building = []
  current_level = [i for i in range(1, unit + 1)]
  building.append(current_level)

  for i in range(floor):
    for j in range(1, unit): #0부터 시작하면 -1호를 접근 : 1호부터 시작
      # 2호까지 계산한다면
      #1 1호에는 0호의 사람과 1호의 사람을 더한 값
      #2 2호에는 1호의 사람과 2호의 사람을 더한 값
      current_level[j] = current_level[j] + current_level[j - 1]
    building.append(current_level)

  people = building.pop().pop()
  print(people)

# 개어렵네