# 문제
# pattern+1개의 I와 N개의 O로 이루어져 있으면,
# I와 O이 교대로 나오는 문자열을 PN이라고 한다.
# - P1 IOI
# - P2 IOIOI
# - P3 IOIOIOI
# - PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때,
# S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다. (1 ≤ pattern ≤ 1,000,000, 2N+1 ≤ M ≤ 1,000,000)
#
# 출력
# S에 PN이 몇 군데 포함되어 있는지 출력한다.


def get_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    begin, matched = 1, 0

    while begin + matched < m:
        if pattern[begin + matched] == pattern[matched]:
            matched += 1
            pi[begin + matched - 1] = matched

        else:
            if matched == 0:
                begin += 1

            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def kmp(S, pattern):
    n, m = len(S), len(pattern)
    result = 0
    pi = get_pi(pattern)
    begin, matched = 0, 0

    while begin <= n - m:
        if matched < m and S[begin + matched] == pattern[matched]:
            matched += 1

            if matched == m:
                result += 1

        else:
            if matched == 0:
                begin += 1

            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

    return result


N = int(input())
M = int(input())
S = input()
pattern = "I" + ("OI" * N)
print(kmp(S, pattern))
