# 문제
# 혁진이는 알고리즘 문제를 만들라는 독촉을 받아 스트레스다.
# 하지만 피보나치 문제는 너무 많이 봐서 지겹기 그지없다.
# 그러나 문제를 만들 시간이 없는 혁진이는 피보나치 문제를 응용해서 문제를 만들려 한다.
# int fibonacci(int n) { // 호출
#   if (n < 2) {
#     return n;
#   }
#   return fibonacci(n-2) + fibonacci(n-1);
# }
# 위와 같이 코딩하였을 때 fibonacci(n)를 입력했을 때에 fibonacci 함수가 호출되는 횟수를 계산해보자.
#
# 입력
# fibonacci 함수에 인자로 입력할 n이 주어진다. (0 ≤ n ≤ 50)
#
# 출력
# fibonacci 함수가 호출된 횟수를 출력한다.
# 출력값이 매우 커질 수 있으므로 정답을 1,000,000,007 로 나눈 나머지를 출력한다.


N = int(input())

dp = [1 for _ in range(51)]
dp[1], dp[2] = 1, 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1] + 1) % 1_000_000_007

print(dp[N])
