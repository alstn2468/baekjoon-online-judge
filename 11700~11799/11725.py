# 문제
# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때,
# 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

parents = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
queue = deque([1])

while queue:
    parent = queue.popleft()

    for node in tree[parent]:
        if not visited[node]:
            parents[node] = parent
            queue.append(node)
            visited[node] = True

for node in parents[2:]:
    print(node)
