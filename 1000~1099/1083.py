# 문제
# 크기가 N인 배열 A가 있다. 배열에 있는 모든 수는 서로 다르다.
# 이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다.
# 그리고, 교환은 많아봐야 S번 할 수 있다.
# 이때, 소트한 결과가 사전순으로 가장 뒷서는 것을 출력한다.
#
# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 각 원소가 차례대로 주어진다.
# 이 값은 1000000보다 작거나 같은 자연수이다.
# 마지막 줄에는 S가 주어진다. S는 1000000보다 작거나 같은 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

N = int(input())
arr = list(map(int, input().split()))
S = int(input())
idx = 0

while S:
    if idx == N:
        break

    i = arr.index(max(arr[idx : idx + S + 1]))
    arr.insert(idx, arr.pop(i))
    S -= i - idx
    idx += 1

print(" ".join(map(str, arr)))
