#
# 문제
# 대열이는 욱제의 친구다.
#   - “야 백대열을 약분하면 뭔지 알아?”
#   - “??”
#   - “십대일이야~ 하하!”
# n:m이 주어진다. 욱제를 도와주자. (...)
#
# 입력
# n과 m이 :을 사이에 두고 주어진다.
# (1 <= n, m <= 100,000,000)
#
# 출력
# 두 수를 최대한으로 약분하여 출력한다.


def get_gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    while n2 != 0:
        n = n1 % n2
        n1 = n2
        n2 = n
    return n1


n, m = map(int, input().split(":"))
gcd = get_gcd(n, m)

print(str(n // gcd) + ":" + str(m // gcd))
