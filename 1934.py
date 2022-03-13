import sys
from math import gcd, floor
input = sys.stdin.readline

repeat = int(input())

for i in range(repeat):
  a, b = map(int, input().strip().split())
  gcd_num = gcd(a, b)
  lcm_num = floor(a * b / gcd_num)
  print(lcm_num)
