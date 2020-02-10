# 문제
# 방향 없는 그래프가 주어졌을 때,
# 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
#
# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.


def bfs(start):
    queue, visited[start] = [start], 1

    while queue:
        now = queue.pop(0)

        for i in edge[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

result = 0

for i in range(1, len(visited)):
    if visited[i] == 0:
        bfs(i)
        result += 1

print(result)
