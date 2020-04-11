# 문제
# N개의 자연수와 자연수 M이 주어졌을 때,
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 둘째 줄에 N개의 수가 주어진다.
# 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

from itertools import combinations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
print(
    "\n".join([" ".join(list(map(str, comb))) for comb in list(combinations(arr, M))])
)
