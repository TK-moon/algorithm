import sys
input = sys.stdin.readline

peoples_per_square_meter, square_meter_party_room = map(int, input().strip().split())
people_count_on_news = list(map(int, input().strip().split()))
people_count = peoples_per_square_meter * square_meter_party_room

arr = list(map(lambda x: x - people_count, people_count_on_news))

print(*arr)