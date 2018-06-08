
# 문제
# nCm을 출력한다.
#
# 입력
# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)
#
# 출력
# nCm을 출력한다.

fact = [[0 for i in range(101)] for j in range(101)]
fact[0][0] = fact[1][0] = fact[1][1] = 1

for i in range(2, 101) :

    for j in range(0, i + 1) :
        
        if i == j or j == 0 :
            fact[i][j] = 1

        elif fact[i][j] == 0 :
            fact[i][j] = fact[i - 1][j - 1] + fact[i - 1][j]

N, K = map(int, input().split())

print(fact[N][K])
