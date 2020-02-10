# 문제
# n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?
#
# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 두 자연수 n(n ≥ 1)과 k(0 ≤ k ≤n)로 이루어져 있다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, 정답을 출력한다. 항상 정답이 2³¹보다 작은 경우만 입력으로 주어진다.


while True:
    n, k = input().split()

    n = int(n)
    k = int(k)

    div = 1
    result = 1

    if n == 0 and k == 0:
        break

    if n - k < k:
        k = n - k

    while k > 0:
        k -= 1
        result *= n
        n -= 1
        result /= div
        div += 1

    print(int(result))
