
# 문제
# 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다.
# 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다.
# 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인
# 직사각형으로 이루어진 히스토그램이다.
# 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.
#
# 입력
# 입력은 테스트 케이스 여러 개로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있고,
# 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000)
# 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1000000000)가 주어진다.
# 이 숫자들은 히스토그램에 있는 직사각형의 높이이며,
# 왼쪽부터 오른쪽까지 순서대로 주어진다.
# 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

import sys

sys.setrecursionlimit(10 ** 6)

def init(array, tree, node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]

    mid = (start + end) // 2
    left = init(array, tree, node * 2, start, mid)
    right = init(array, tree, node * 2 + 1, mid + 1, end)

    if array[left] < array[right]:
        tree[node] = left

    else:
        tree[node] = right

    return tree[node]


def query(array, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    left_index = query(array, tree, node * 2,
                       start, (start + end) // 2, left, right)
    right_index = query(array, tree, node * 2 + 1,
                        (start + end) // 2 + 1, end, left, right)

    if left_index == -1 and right_index == -1:
        return -1

    elif left_index == -1:
        return right_index

    elif right_index == -1:
        return left_index

    else:
        if array[left_index] < array[right_index]:
            return left_index

        return right_index


def get_max_area(heights, tree, start, end):
    n = len(heights)
    m = query(heights, tree, 1, 0, n - 1, start, end)
    area = (end - start + 1) * heights[m]

    if start <= m - 1:
        temp = get_max_area(heights, tree, start, m - 1)
        if area < temp:
            area = temp

    if m + 1 <= end:
        temp = get_max_area(heights, tree, m + 1, end)

        if area < temp:
            area = temp

    return area


while True:
    histogram = list(map(int, sys.stdin.readline().split()))

    if histogram == [0]:
        break

    histogram = histogram[1:]

    tree = [0 for _ in range(len(histogram) * 4)]
    segment_tree = init(histogram, tree, 1, 0, len(histogram) - 1)

    print(get_max_area(histogram, tree, 0, len(histogram) - 1))
