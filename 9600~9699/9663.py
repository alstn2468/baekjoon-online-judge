# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


def check(x, y, i, j):
    if x == i or y == j or abs(x - i) == abs(y - j):
        return False

    return True


def solution(d, queen, board):
    if d == N:
        return 1

    else:
        count = 0

        for i in [y for y in range(N) if board[y] == True]:
            flag = True

            for x, y in queen:
                flag = check(x, y, d + 1, i)

                if not flag:
                    break

            if flag:
                temp = board.copy()
                temp[i] = False
                count += solution(d + 1, queen + [(d + 1, i)], temp)

        return count


N = int(input())
print(solution(0, [], [True for _ in range(N)]))
