change = 1000 - int(input())
count = 0

while change > 0:
  if change // 500 > 0:
    count += change // 500
    change = change % 500
  elif change // 100 > 0:
    count += change // 100
    change = change % 100
  elif change // 50 > 0:
    count += change // 50
    change = change % 50
  elif change // 10 > 0:
    count += change // 10
    change = change % 10
  elif change // 5 > 0:
    count += change // 5
    change = change % 5
  elif change // 1 > 0:
    count += change // 1
    change = change % 1

print(count)
