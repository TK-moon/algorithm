n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2 * i, n + 1, i):
        a[j] = False
print(primes)


table = [False, False] + [True] * 10000  
for i in range(2, 101):
    if table[i] == True:
        for j in range(i + i, 10001, i):
            table[j] = False