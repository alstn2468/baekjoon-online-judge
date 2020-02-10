# 문제
# A+B를 계산하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)
#
# 출력
# 첫째 줄에 A+B를 출력한다.

A, B = map(list, map(lambda x: x[::-1], input().split()))

if len(A) > len(B):
    max_size = len(A)
    min_size = len(B)

else:
    max_size = len(B)
    min_size = len(A)

result = [0 for _ in range(max_size)]
carry = 0

for i in range(min_size):
    sum = int(A[i]) + int(B[i]) + carry

    if sum >= 10:
        result[i] = sum % 10
        carry = 1

    else:
        result[i] = sum
        carry = 0

for i in range(min_size, max_size):
    if len(A) > len(B):
        sum = int(A[i]) + carry

        if sum >= 10:
            result[i] = sum % 10
            carry = 1

        else:
            result[i] = sum
            carry = 0

    else:
        sum = int(B[i]) + carry

        if sum >= 10:
            result[i] = sum % 10
            carry = 1

        else:
            result[i] = sum
            carry = 0

if carry == 1:
    print("1", end="")

print("".join(list(map(str, result[::-1]))))
