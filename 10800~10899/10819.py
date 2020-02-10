# 문제
# N개의 정수로 이루어진 배열 A가 주어진다.
# 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
#
# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다.
# 둘째 줄에는 배열 A에 들어있는 정수가 주어진다.
# 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

import itertools

N = int(input())
permus = itertools.permutations(list(map(int, input().split())))
result = 0

for permu in permus:
    temp = 0

    for i in range(N - 1):
        temp += abs(permu[i] - permu[i + 1])

    result = max(temp, result)

print(result)
