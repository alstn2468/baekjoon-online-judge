
# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 차례대로 별을 출력한다.

N = int(input())
count = 0

for i in range(0, (N - 1) * 4 + 1):
    print("*", end="")
print()

for i in range(2, 2 * N):
    for j in range(count + 1):
        print("*", end=" ")

    if i % 2 == 1:
        temp = (N - i + count + 1) * 4 + 1

        for k in range(0, temp):
            print('*', end="")

    elif i % 2 == 0:
        temp = (N - i + count) * 4 + 1

        for k in range(0, temp):
            print(" ", end="")

    for j in range(0, count + 1):
        print(" ", end="*")

    if i % 2 == 1:
        count += 1
    print()

count -= 1

for i in range(2, 2 * N - 1):
    for j in range(0, count + 1):
        print("*", end=" ")

    if i % 2 == 1:
        temp = (i - N + count + 1) * 4 + 1

        for j in range(0, temp):
            print("*", end="")

    elif i % 2 == 0:
        temp = (i - N + count) * 4 + 1

        for j in range(0, temp):
            print(" ", end="")

    for j in range(0, count + 1):
        print(" ", end="*")

    if i % 2 == 0:
        count -= 1

    print()

    if (i >= (2 * N - 2)):
        temp = (N - 1) * 4 + 1

        for j in range(0, temp):
            print("*", end="")
        print()
