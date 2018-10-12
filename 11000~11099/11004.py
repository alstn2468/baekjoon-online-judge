
# 문제
# 수 N개 A1, A2, ..., AN이 주어진다.
# A를 오름차순 정렬했을 때,
# 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
#
# 출력
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

import random, sys

def nth_element(arr, n) :
    left, right = 0, len(arr) - 1

    if not left <= n - 1 <= right :
        raise ValueError('n(%d) must be in [1, %d]' % n, len(arr))

    while left < right :
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right) :
            if arr[i] < pivot_value :
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[store_index], arr[right] = arr[right], arr[store_index]

        if n - 1 == store_index :
            return arr[store_index]

        elif n - 1 < store_index :
            right = store_index - 1

        else :
            left = store_index + 1

    return arr[left]


N, K = map(int, sys.stdin.readline().split())
A = sys.stdin.readline().split()

for i in range(len(A)) :
    A[i] = int(A[i])

print(nth_element(A, K))
