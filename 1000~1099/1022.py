# 크기가 무한인 정사각형 모눈종이가 있다.
# 모눈종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.
# 이 모눈종이 전체를 양의 정수의 소용돌이 모양으로 채울 것이다.
# 일단 숫자 1을 0행 0열에 쓴다.
# 그리고 나서 0행 1열에 숫자 2를 쓴다.
# 거기서 부터 소용돌이는 반시계 방향으로 시작된다.
# 다음 숫자는 다음과 같이 채우면 된다.
#
#     -3 -2 -1  0  1  2  3
#     --------------------
# -3 |37 36 35 34 33 32 31
# -2 |38 17 16 15 14 13 30
# -1 |39 18  5  4  3 12 29
#  0 |40 19  6  1  2 11 28
#  1 |41 20  7  8  9 10 27
#  2 |42 21 22 23 24 25 26
#  3 |43 44 45 46 47 48 49
#
# 이 문제는 위와 같이 채운 것을 예쁘게 출력하면 된다.
# r1, c1, r2, c2가 입력으로 주어진다.
# r1, c1은 가장 왼쪽 위 칸이고, r2, c2는 가장 오른쪽 아래 칸이다.
# 예쁘게 출력한다는 것은 다음과 같이 출력하는 것이다.
# 1. 출력은 r1행부터 r2행까지 차례대로 출력한다.
# 2. 각 원소는 공백으로 구분한다.
# 3. 모든 행은 같은 길이를 가져야 한다.
# 4. 공백의 길이는 최소로 해야 한다.
# 5. 모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 한다.
# 6. 만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.
#
# 입력
# 첫째 줄에 r1, c1, r2, c2가 주어진다.
# 모두 절대값이 5000보다 작거나 같은 정수이고,
# r2 - r1은 0보다 크거나 같고, 49보다 작거나 같으며,
# c2 - c1은 0보다 크거나 같고, 4보다 작거나 같다.
#
# 출력
# r2 - r1 + 1개의 줄에 소용돌이를 예쁘게 출력한다.

import sys

sys.setrecursionlimit(10 ** 6)


def get_number(x, y, ends):
    num = 1
    if x == y == 0:
        return num

    (big, small) = (x, y) if abs(x) >= abs(y) else (y, x)
    corners = []

    width = abs(big) * 2 + 1

    corners.append(ends[width - 2] + width - 1)

    for _ in range(3):
        corners.append(corners[-1] + width - 1)

    if x == y and x > 0:
        return corners[3]

    elif x == y and x < 0:
        return corners[1]

    elif x + y == 0 and x < 0:
        return corners[2]

    elif x + y == 0 and x > 0:
        return corners[0]

    if x == big and x > 0:
        num = corners[0] - (x + y)

    elif x == big and x < 0:
        num = corners[2] + (x + y)

    elif y == big and y > 0:
        num = corners[3] - (y - x)

    else:
        num = corners[1] + (y - x)

    return num


def get_spiral(y1, x1, y2, x2, ends):
    spiral = []
    spiral_str = []
    max_lengths = 0

    for y in range(y1, y2 + 1):
        row = []

        for i, x in enumerate(range(x1, x2 + 1)):
            num = get_number(x, y, ends)
            row.append(num)
            max_lengths = max(max_lengths, len(str(num)))

        spiral.append(row)

    for row in spiral:
        row_str = []

        for i, n in enumerate(row):
            f_str = "{0:" + str(max_lengths) + "d}"
            row_str.append(f_str.format(row[i]))
        spiral_str.append(" ".join(row_str))

    return "\n".join(spiral_str)


if __name__ == "__main__":
    ends = [0] * 10002
    ends[1] = 1

    for w in range(3, 10002, 2):
        ends[w] = ends[w - 2] + w * 2 + (w - 2) * 2

    r1, c1, r2, c2 = list(map(int, sys.stdin.readline().strip().split(" ")))

    print(get_spiral(r1, c1, r2, c2, ends))
