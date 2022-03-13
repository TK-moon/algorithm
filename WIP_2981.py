## 시간초과

# import sys
# input = sys.stdin.readline

# repeat = int(input())

# numbers = [0] * repeat

# for i in range(repeat):
#   numbers[i] = int(input().strip())

# numbers.sort()

# for i in range(2, max(numbers) // 2 + 1):
#   flag = True
#   left = numbers[0] % i

#   for index in range(1, len(numbers)):
#     if left != numbers[index] % i:
#       flag = False
#       break

#   if flag: print(i, end=' ')
