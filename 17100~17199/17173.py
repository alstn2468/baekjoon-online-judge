
# 문제
# 신원이는 백준에서 배수에 관한 문제를 풀다가 감명을 받아 새로운 문제를 만들어보았다.
# 자연수 N과 M개의 자연수 Ki가 주어진다.
# Ki중 적어도 하나의 배수이면서 1 이상 N 이하인 수의 합을 구하여라.
#
# 입력
# 첫 번째 줄에 N과 M가 주어진다. (2 ≤ N ≤ 1000, 1 ≤ M < N)
# 그다음 줄에 M개의 정수 Ki가 주어진다. (2 ≤ Ki ≤ 1000)
# 동일한 Ki는 주어지지 않으며, 오름차순으로 정렬되어있다.
#
# 출력
# 배수들의 합을 출력한다.

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum = 0

for i in range(1, N + 1):
    for num in nums:
        if i % num == 0:
            sum += i
            break

print(sum)
