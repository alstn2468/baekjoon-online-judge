# 문제
# 자연수 n개가 주어진다.
# 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n이 주어진다. n은 2 또는 3이다.
# 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다.
# 모든 자연수는 108 이하이다.
#
# 출력
# 입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
flatten = sum([[i for i in range(1, num + 1) if num % i == 0] for num in nums], [])
result = set(list(filter(lambda x: flatten.count(x) == n, flatten)))
for i in result: print(i)
