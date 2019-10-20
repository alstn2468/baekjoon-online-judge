
# 문제
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
# 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
# 2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
# 2 1 0 0 1 1 0
# 1 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 1 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
# 2 1 0 0 1 1 2
# 1 0 1 0 1 2 2
# 0 1 1 0 1 2 2
# 0 1 0 0 0 1 2
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.
# 위의 지도에서 안전 영역의 크기는 27이다.
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.

# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

import copy
import sys

input = sys.stdin.readline


def spread_virus(virus_list, copy_maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    spread_virus_count = 0
    global safe_area

    while virus_list:
        x, y = virus_list.pop()

        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])

            if 0 <= nx and 0 <= ny and nx < N and ny < M:
                if copy_maps[nx][ny] == 0:
                    copy_maps[nx][ny] = 2
                    spread_virus_count += 1
                    virus_list.add((nx, ny))

    return safe_area - spread_virus_count - 3


def set_wall(start,  wall_count):
    global result
    global N
    global M

    if wall_count == 0:
        copy_maps = copy.deepcopy(maps)
        copy_virus_list = copy.deepcopy(virus_list)

        cnt = spread_virus(copy_virus_list, copy_maps)
        result = max(cnt, result)

        return

    for i in range(start, N * M):
        x = i // M
        y = i % M

        if maps[x][y] == 0:
            maps[x][y] = 1
            set_wall(i + 1, wall_count - 1)
            maps[x][y] = 0


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
virus_list = set()
result, safe_area = 0, 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus_list.add((i, j))

        elif maps[i][j] == 0:
            safe_area += 1

set_wall(0, 3)
print(result)
