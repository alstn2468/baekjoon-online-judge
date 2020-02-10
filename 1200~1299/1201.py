# 문제
# 1부터 N까지의 수를 한 번씩 이용해서 최대 부분 증가 수열의 길이가 M이고,
# 최대 부분 감소 수열의 길이가 K인 수열을 출력한다.
#
# 입력
# 첫째 줄에 N M K가 주어진다.
# N은 500보다 작거나 같은 자연수, M과 K는 N보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 정답이 없다면-1을 출력한다

N, M, K = map(int, input().split())

if M + K - 1 <= N <= M * K:
    nums, boundary = [i + 1 for i in range(N)], [0, K]
    N, M = N - K, M - 1
    if M == 0:
        group_size, remainder = 1, 0

    else:
        group_size, remainder = N // M, N % M

    for i in range(M):
        if remainder > 0:
            boundary.append(boundary[-1] + group_size + 1)
            remainder -= 1

        else:
            boundary.append(boundary[-1] + group_size)

    for i in range(len(boundary) - 1):
        nums[boundary[i] : boundary[i + 1]] = nums[boundary[i] : boundary[i + 1]][::-1]

    print(" ".join(map(str, nums)))

else:
    print(-1)
