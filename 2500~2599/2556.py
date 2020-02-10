# 문제
# 지금까지 안나온 별 찍기가 뭐가 있는지 생각해본 후, 별을 적절히 찍으세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# N개의 줄에 걸쳐 별을 적절히 찍는다.

n = int(input())

for _ in range(n):
    for _ in range(n):
        print("*", end="")
    print()
