/*
	*
	*	문제
	*	N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
	*
	*	출력
	*	첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
	*
*/

#include <stdio.h>


int main()
{
	int test_case;
	int input;
	int num[10001] = { 0 };

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%d", &input);
		num[input]++;
	}

	for (int i = 1; i <= 10000; i++)
	{
		if (num[input] > 0)
		{
			for (int j = 0; j <num[i]; j++)
			{
				printf("%d\n", i);
			}
		}
	}

	return 0;
}
