nums = []
for i in range(5):
  num = max(int(input()), 40)
  nums.append(num)

print(int(sum(nums) / 5))