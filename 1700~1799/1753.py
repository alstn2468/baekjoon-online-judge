# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.
#
# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000)
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다.
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
# u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
#
# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

import sys
from heapq import heappush, heappop

r = sys.stdin.readline
INF = sys.maxsize


def dijkstra(v, k, g):
    dist = [INF for _ in range(v)]
    dist[k - 1] = 0
    q = []
    heappush(q, [0, k - 1])

    while q:
        cost, pos = heappop(q)

        for p, c in g[pos]:
            c += cost

            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])

    return dist


V, E = map(int, r().split())
K = int(r())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, r().split())
    graph[u - 1].append([v - 1, w])

for d in dijkstra(V, K, graph):
    print(d if d != INF else "INF")
