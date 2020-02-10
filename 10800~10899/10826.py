# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n이 주어진다. n은 10,000보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.


def big_num_calc(num_a, num_b):
    A, B = list(num_a)[::-1], list(num_b)[::-1]

    if len(A) > len(B):
        max_size, min_size = len(A), len(B)

    else:
        max_size, min_size = len(B), len(A)

    result = [0 for _ in range(max_size)]
    carry = 0

    for i in range(min_size):
        sum = int(A[i]) + int(B[i]) + carry

        if sum >= 10:
            result[i] = str(sum % 10)
            carry = 1

        else:
            result[i] = str(sum)
            carry = 0

    for i in range(min_size, max_size):
        if len(A) > len(B):
            sum = int(A[i]) + carry

        else:
            sum = int(B[i]) + carry

        if sum >= 10:
            result[i] = str(sum % 10)
            carry = 1

        else:
            result[i] = str(sum)
            carry = 0

    if carry == 1:
        result.append("1")

    return "".join(reversed(result))


dp = ["0" for _ in range(10001)]
n = int(input())

dp[1] = "1"

for i in range(2, n + 1):
    dp[i] = big_num_calc(dp[i - 1], dp[i - 2])

print(dp[n])
