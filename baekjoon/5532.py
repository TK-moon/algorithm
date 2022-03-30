import math
vacation = int(input())

k = int(input())
m = int(input())

kor_can_per_day = int(input())
math_can_per_day = int(input())

kor_duration = k / kor_can_per_day
math_duration = m / math_can_per_day

max_day = max(kor_duration, math_duration)
print(vacation - math.ceil(max_day))