# 1 내가 푼 문제

current_time, current_minute = map(int, input().split(' '))
cook_duration = int(input())

overtime = 0

current_minute += cook_duration

if 60 <= current_minute:
  overtime = current_minute // 60
  current_time += overtime
  current_minute = current_minute - (60 * overtime)

if (current_time >= 24):
  current_time = current_time - 24

print(current_time, current_minute)





# 2 인터넷에 올라와 있는 문제 풀이 // 더 깔끔하다

# hour, minute = map(int, input().split())
# duration = int(input())

# hour += duration // 60
# minute += duration % 60

# if minute >= 60 :
#     hour += 1
#     minute -= 60

# if hour >= 24 :
#     hour -= 24

# print('%d %d' % (hour, minute))