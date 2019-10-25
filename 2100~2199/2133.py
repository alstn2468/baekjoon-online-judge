
# 문제
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다.

N = int(input())
dp = [1, *([0] * N)]

for i in range(2, N + 1, 2):
    dp[i] = dp[i - 2] * 3

    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[N])
