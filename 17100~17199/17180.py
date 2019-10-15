
# 문제
# 두 문자열을 비교하는 방법이 다음과 같은 두 가지 규칙을 따를 때,
# 두 문자열 간 차이의 최솟값이 얼마가 되는지를 구해보려 한다.
# 첫 번째로 각 문자 간의 차이는 알파벳 순서의 차이의 절댓값과 같다.
# 예를 들어, a는 첫 번째 알파벳이고 c는 세 번째 알파벳이므로, a와 c의 차이는 | 1-3 | = 2이다.
# 마찬가지로 a와 z의 차이는 | 1 - 26 | = 25이다.
# 두 번째 규칙은 두 문자열의 각 알파벳을 늘이는 것이 가능하다는 것이다.
# 위 두 규칙을 이용해 두 문자열의 문자 간 차이의 합을 구하면 문자열의 차이가 된다.
# 예를 들어 apple과 aple이 주어질 때, aple의 p를 늘려 apple로 만들 수 있다.
# 이 경우 두 문자열의 차이는 0이다. 임의의 두 문자열이 주어질 때, 두 문자열의 차이가 최소가 되는 값을 구해라.
# 단, 두 문자열에서 문자 간의 차이의 합을 구할 때는 반드시 두 문자열의 길이를 동일하게 만들어서 계산해야 한다.
#
# 입력
# 첫 번째 줄에는 2개의 문자열의 길이인 N와 M가 주어진다. (1 ≤ N, M ≤ 300)
# 두 번째 줄에는 첫 번째 문자열이 주어진다.
# 세 번째 줄에는 두 번째 문자열이 주어진다.
# 단, 문자열에는 a~z까지의 알파벳 소문자만 주어진다.
#
# 출력
# 두 문자열 간 차이의 최솟값을 구한다.


def solution(a_idx, b_idx):
    if dp[a_idx][b_idx] != -1:
        return dp[a_idx][b_idx]

    result = 999999

    if a_idx < N - 1:
        result = min(result, solution(a_idx + 1, b_idx))

    if b_idx < M - 1:
        result = min(result, solution(a_idx, b_idx + 1))

    if a_idx < N - 1 and b_idx < M - 1:
        result = min(result, solution(a_idx + 1, b_idx + 1))

    dp[a_idx][b_idx] = result + abs(B[b_idx] - A[a_idx])

    return dp[a_idx][b_idx]


N, M = map(int, input().split())
A, B = list(map(ord, list(input()))), list(map(ord, list(input())))
dp = [[-1 for _ in range(max(N, M))] for _ in range(max(N, M))]
dp[N - 1][M - 1] = abs(A[N - 1] - B[M - 1])
print(solution(0, 0))
