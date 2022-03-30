user_input = input().split()

a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)