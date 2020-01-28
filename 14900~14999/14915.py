
# 문제
# 정수 m, n을 입력 받아, 10진수 m을 n진수로 바꾸어 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에서 정수 m, n을 입력 받는다. (0 ≤ m ≤ 1,000,000, 2 ≤ n ≤ 16)
#
# 출력
# 변환한 n진수의 수를 출력한다.
# 11~16 진수의 경우 10 이상의 수는 A~F 문자를 사용한다.
# 예를 들어, 10은 A, 11은 B, 12는 C, 13은 D, 14는 E, 15는 F를 사용한다.


def convert(number, base):
    CHARS = "0123456789ABCDEF"
    i, j = divmod(number, base)

    if i == 0:
        return CHARS[j]

    else:
        return convert(i, base) + CHARS[j]


M, N = map(int, input().split())
print(convert(M, N))
