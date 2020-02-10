# 문제
# 문제는 매우 간단하다. N을 N번 출력하는 프로그램을 작성하여라.
# 다만, 답이 길어지는 경우 답의 앞 M자리만 출력한다.
#
# 입력
# 첫 번째 줄에는 N, M이 주어진다. (1 ≤ N, M ≤ 2016)
#
# 출력
# N을 N번 출력한다. 만약 답이 길어지면 답의 앞 M자리를 출력한다.

N, M = map(int, input().split())

str_N, size = str(N), len(str(N))

if size * N > M:
    end = M // size

    for i in range(end):
        print(N, end="")

    end = M % size

    for i in range(end):
        print(str_N[i], end="")

else:
    for i in range(int(N)):
        print(N, end="")

print()
