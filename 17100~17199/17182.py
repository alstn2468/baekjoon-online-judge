
# 문제
# 우주 탐사선 ana호는 어떤 행성계를 탐사하기 위해 발사된다.
# 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하려 한다.
# 입력으로는 ana호가 탐색할 행성의 개수와 ana호가 발사되는 행성의 위치와
# ana호가 행성 간 이동을 하는데 걸리는 시간이 2차원 행렬로 주어진다.
# 행성의 위치는 0부터 시작하여 0은 행렬에서 0번째 인덱스에 해당하는 행성을 의미한다.
# 2차원 행렬에서 i, j 번 요소는 i 번째 행성에서 j 번째 행성에 도달하는데 걸리는 시간을 나타낸다.
# i와 j가 같을 때는 항상 0이 주어진다. 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하여라.
# 탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.
#
# 입력
# 첫 번째 줄에는 행성의 개수 N과 ana호가 발사되는 행성의 위치 K가 주어진다. (2 ≤ N ≤ 10, 0 ≤ K < N)
# 다음 N 줄에 걸쳐 각 행성 간 이동 시간 Tij 가 N 개 씩 띄어쓰기로 구분되어 주어진다. (0 ≤ Tij  ≤ 1000)
#
# 출력
# 모든 행성을 탐사하기 위한 최소 시간을 출력한다.


def solution(cur, mm):
    if mm == ((2 ** N) - 1):
        return 0

    if dp[cur][mm] != -1:
        return dp[cur][mm]

    result = 99999999

    for i in range(N):
        if (mm & (1 << i)) == 0:
            result = min(result, solution(i, mm + (2 ** i)) + T[cur][i])

    dp[cur][mm] = result

    return dp[cur][mm]


N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(2 ** N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            T[i][j] = min(T[i][j], T[i][k] + T[k][j])

print(solution(K, 2 ** K))
