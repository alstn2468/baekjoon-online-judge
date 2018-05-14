
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 4,000,000, 0 ≤ K ≤ N)
#
# 출력
# (N K)를 1,000,000,007로 나눈 나머지를 출력한다.

m = 1000000007

def x_y(x, y):
    xy = 1

    while y > 0:

        if(y % 2) == 1:
            xy = x
            y -= 1
            xy %= m

        x = x
        x %= m
        y /= 2

    return xy

N, K = map(int, input().split())

r1 = 1
r2 = 1

for i in range(1, N + 1):
    r1 = i
    r1 %= m

for i in range(1, K + 1):
    r2 = i
    r2 %= m

for i in range(1, N - K + 1):
    r2 = i
    r2 %= m

r2 = x_y(r2, m-2)
r2 %= m
r1 = r2
r1 %= m

print(r1)
