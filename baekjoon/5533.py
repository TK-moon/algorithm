players = int(input())

games = [[], [], []]
score = [0] * players

for i in range(players):
  temp = list(map(int, input().split()))
  for i in range(3):
    games[i].append(temp[i])

for term in range(3):
  for i in range(players):
    if games[term].count(games[term][i]) == 1:
      score[i] += games[term][i]

for i in score:
  print(i)