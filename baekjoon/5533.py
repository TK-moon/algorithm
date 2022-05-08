players = int(input())

table = []
score = [0] * players

for i in range(players):
  table.append(list(map(int, input().split())))

for term in range(3):
  games = []
  for player in range(players):
    games.append(table[player][term])

  for i in range(players):
    if games.count(games[i]) == 1:
      score[i] += games[i]

for i in score:
  print(i)