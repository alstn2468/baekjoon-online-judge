/*
	*
	*	문제
	*	자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 구하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
	*
	*	출력
	*	(N K)를 출력한다.
	*
*/

#include <stdio.h>

int Sol(int N, int K)
{
	if (N == K || K == 0)
		return 1;
	else
		return Sol(N - 1, K - 1) + Sol(N - 1, K);
}

int main()
{
	int N, K;

	scanf("%d %d", &N, &K);

	printf("%d\n", Sol(N, K));

	return 0;
}
