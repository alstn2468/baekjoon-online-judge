
# 문제
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.
#
# 출력
# 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

from itertools import permutations

arr = [i for i in range(1, int(input()) + 1)]
print('\n'.join([' '.join(map(str, perm))
                 for perm in permutations(arr, len(arr))]))
