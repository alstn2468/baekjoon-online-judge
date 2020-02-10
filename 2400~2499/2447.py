# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N이 주어진다.
# N은 항상 3의 제곱꼴인 수이다. (1, 3, 9, 27, ...) (N=3k, 0 ≤ k < 8)
#
# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.


def draw_star(mod, i, j):
    if (i // mod) % 3 == 1 and (j // mod) % 3 == 1:
        print(" ", end="")

    else:
        if mod // 3 == 0:
            print("*", end="")

        else:
            draw_star(mod // 3, i, j)


n = int(input())

for i in range(n):
    for j in range(n):
        draw_star(n, i, j)
    print()
