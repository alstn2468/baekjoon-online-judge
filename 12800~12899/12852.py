
# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다.
# 정답이 여러 가지인 경우에는 아무거나 출력한다.

N = int(input())

result = [[0, []] for _ in range(N + 1)]
result[1][0] = 0
result[1][1] = [1]

for i in range(2, N + 1):
    result[i][0] = result[i - 1][0] + 1
    result[i][1] = result[i - 1][1] + [i]

    if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
        result[i][0] = result[i // 3][0] + 1
        result[i][1] = result[i // 3][1] + [i]

    if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
        result[i][0] = result[i // 2][0] + 1
        result[i][1] = result[i // 2][1] + [i]

print(result[N][0])

for i in result[N][1][::-1]:
    print(i, end=' ')
