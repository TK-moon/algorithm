def solution(x):
    # y = sum(map(int, str(x)))
    # return False if x % y else True
    return x % sum(int(n) for n in str(x)) == 0