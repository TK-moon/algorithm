# def solution(x, n):
#     if n == 0: return []
#     if x == 0: return [x] * n
#     end = (x * n) + x
#     answer = list(range(x, end, x))
#     return answer

def solution(x, n):
    return [i * x + x for i in range(n)]