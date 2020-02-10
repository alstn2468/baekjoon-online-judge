# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 차례대로 별을 출력한다.

N = int(input())

if N == 1:
    print("*")

else:
    for i in range(1, 2 * N + 1):
        for j in range(1, N + 1):
            if (i + j) % 2 == 0:
                print("*", end="")

            else:
                print(" ", end="")

        print()
