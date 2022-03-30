user_input = input().split()
A = input().split()

N = int(user_input[0])
X = int(user_input[1])

for i in range(0, N):
	if (int(A[i]) < X):
		print(A[i])