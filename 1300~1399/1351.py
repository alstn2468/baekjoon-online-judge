# 문제
# 무한 수열 A는 다음과 같다.
# A0 = 1
# Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
# N, P와 Q가 주어질 때, AN을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 3개의 정수 N, P, Q가 주어진다.
#
# 출력
# 첫째 줄에 AN을 출력한다.
#
# 제한
# 0 ≤ N ≤ 1012
# 2 ≤ P, Q ≤ 109

dp = {0: 1}


def solution(N, P, Q):
    if N == 0:
        return 1

    if N in dp:
        return dp[N]

    dp[N] = solution(N // P, P, Q) + solution(N // Q, P, Q)

    return dp[N]


N, P, Q = map(int, input().split())
print(solution(N, P, Q))
