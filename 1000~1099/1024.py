
# 문제
# N과 L이 주어질 때, 합이 N이면서,
# 길이가 적어도 L이면서 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 L이 주어진다.
# N은 1000000000보다 작거나 같은 자연수이고,
# L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.
#
# 출력
# 만약 리스트의 길이가 100보다 작거나 같으면,
# 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다.
# 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

def get_gcd(n1, n2) :
    if n1 < n2 :
        n1, n2 = n2, n1

    while n2 != 0 :
        N = n1 % n2
        n1 = n2
        n2 = N

    return n1

def int_series(N, L) :
    series = []

    if N % L == 0 and L % 2 == 1 :
        series = [N // L] * L
        mid = len(series) // 2

        for i in range(1, mid + 1) :
            series[mid-i] -= i
            series[mid+i] += i

    elif L % 2 == 0 and L // get_gcd(N, L) == 2 :
        series = [N / L] * L
        mid = len(series) // 2

        for i in range(mid) :
            series[mid + i] += (i + 0.5)
            series[mid - i - 1] -= (0.5 + i)

        series = [int(N) for N in series]

    return series if all(N >= 0 for N in series) else 0

N, L = map(int, input().split())
check = False

while L <= 100 :
    series = int_series(N, L)

    if series :
        check = True
        break

    else :
        L += 1

if check :
    answer = ''

    for N in series :
        answer += str(N) + ' '

    print(answer.rstrip())

else :
    print(-1)
