/*
	*
	*	문제
	*	n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
	*
	*	출력
	*	1부터 n까지 합을 출력한다.
	*
*/

#include <stdio.h>

int main()
{
	int num, total = 0;

	scanf("%d", &num);

	for (int i = 0; i <= num; i++)
		total += i;

	printf("%d\n", total);

	return 0;
}
