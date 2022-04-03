def solution(phone_number):
  length = len(phone_number) - 4
  return '*' * length + phone_number[-4:]