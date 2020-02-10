# 문제
# N×N크기의 행렬로 표현되는 종이가 있다.
# 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다.
# 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고,
# 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수,
# 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다.
# 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
#
# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를,
# 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.


def nine_range(paper):
    n = len(paper[0])
    size = n // 3
    part = [range(size), range(size, n - size), range(n - size, n)]
    nine_paper = []

    for x in part:
        for y in part:
            nine_paper.append([[paper[i][j] for i in y] for j in x])

    return nine_paper


def solution(paper):
    flat_paper = [item for sub in paper for item in sub]

    if len(set(flat_paper)) <= 1:
        num_count[flat_paper[0] + 1] += 1

    else:
        for part_paper in nine_range(paper):
            solution(part_paper)


import sys

n = int(sys.stdin.readline())

paper = []
num_count = [0, 0, 0]

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

solution(paper)

for count in num_count:
    print(count)
