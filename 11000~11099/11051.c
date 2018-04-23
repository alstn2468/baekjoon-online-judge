/*
	*
	*	문제
	*	자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)
	*
	*	출력
	*	(N K)를 10,007로 나눈 나머지를 출력한다.
	*
*/

#include <stdio.h>
#define MOD 10007
#define NMAX 1001

typedef long long int ll;
ll dp[NMAX][NMAX];

void makePascalTriangle()
{
	dp[0][0] = 1;

	for (int i = 1; i < NMAX; i++)
	{
		dp[i][0] = 1;

		for (int j = 1; j <= i; j++)
			dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
	}
}

ll nCr(int n, int k)
{
	return dp[n][k];
}

int main()
{
	int n, k;

	makePascalTriangle();

	scanf("%d %d", &n, &k);
	printf("%lld\n", nCr(n, k));

	return 0;
}
