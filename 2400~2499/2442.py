
# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ...,
# N번째 줄에는 별 2×N-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

n = int(input())

for i in range(1, n + 1):
    for left in range(n - i):
        print(' ', end="")

    for star in range(2 * i - 1):
        print('*', end="")

    print()
