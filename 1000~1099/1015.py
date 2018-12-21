
# 문제
# P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다.
# 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.
# 배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오.
# 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다.
# 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.
#
# 입력
# 첫째 줄에 배열 A의 크기 N이 주어진다.
# 둘째 줄에는 배열 A의 원소가 0번부터 차례대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 비내림차순으로 만드는 수열 P를 출력한다.

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = {}

for i, a in enumerate(sorted(A)):
    if a in result:
        if type(result[a]) is int:
            result[a] = [result[a], i]

        else:
            result[a].append(i)

    else:
        result[a] = i

for a in A:
    if type(result[a]) is list:
        print(result[a].pop(0), end=' ')

    else:
        print(result[a], end=' ')
