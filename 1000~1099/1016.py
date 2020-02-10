# 문제
# 어떤 수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 제곱ㄴㄴ수라고 한다.
# 제곱수는 정수의 제곱이다. min과 max가 주어지면,
# min과 max를 포함한 사이에 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
#
# 입력
# 첫째 줄에 min과 max가 주어진다.
# min은 1보다 크거나 같고, 1,000,000,000,000보다 작거나 같은 자연수이고,
# max는 min보다 크거나 같고, min+1,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 [min,max]구간에 제곱ㄴㄴ수가 몇 개인지 출력한다.

import sys

min, max = map(int, sys.stdin.readline().split())

num = [True for _ in range(min, max + 1)]
count = len(num)
n = 2

while n ** 2 <= max:
    square = n ** 2
    i = min // square

    while square * i <= max:
        idx = square * i - min

        if idx >= 0 and num[idx]:
            count -= 1
            num[idx] = False

        i += 1
    n += 1

print(count)
