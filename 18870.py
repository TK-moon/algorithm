import sys
input = sys.stdin.readline

repeat = int(input())
arr = list(map(int, input().split()))

setted_arr = list(set(arr))
setted_arr.sort()

dic = { setted_arr[i] : i for i in range(len(setted_arr)) }

print(*[dic[i] for i in arr])

# 인터넷 풀이 참고함
# 어떻게 이런 생각을 하지

# 정리
# 1. 입력받은 배열에서 중복을 제거
# 2. 중복 제거된 배열 정렬
# 3. 중복 제거된 배열으로 for 문을 돌면서 딕셔너리에 값을 입력
# 3-1. 딕셔너리의 key는 배열의 값, value는 반복문의 반복 순서를 넣는다
# 3-2. 이렇게 하면, 가장 작은 수부터 큰 수까지 몇번째로 작은 값인지 key, value 쌍으로 저장 가능
# 4. 원본 배열으로 for문을 돌면서 원본 배열의 값으로 딕셔너리 key를 조회하면 딕셔너리의 value 조회 가능
# 5. 딕셔너리의 value는 3-2 에서 저장한 value 값