def solution(arr1, arr2):
    # outer = len(arr1)
    # inner = len(arr1[0])
    # result = []
    # for i in range(outer):
    #     arr = []
    #     for j in range(inner):
    #         sum = arr1[i][j] + arr2[i][j]
    #         arr.append(sum)
    #     result.append(arr)
    # return result
    
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]