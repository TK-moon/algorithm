repeat = int(input())

cute_count = 0
not_cute_count = 0
for _ in range(repeat):
  answer = int(input())
  if answer: cute_count += 1
  else: not_cute_count += 1

if cute_count < not_cute_count: print('Junhee is not cute!')
else: print('Junhee is cute!')