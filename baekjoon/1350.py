input()
files = list(map(int, input().split()))
cluster = int(input())
count = 0

for file in files:
  if file == 0: continue
  count += file // cluster
  if (file % cluster): count += 1

print(count * cluster)