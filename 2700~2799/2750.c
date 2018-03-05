/*
	*
	*	문제
	*	N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 수의 개수 N(1<=N<=1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
	*	이 수는 절대값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
	*
	*	출력
	*	첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
	*
*/

#include <stdio.h>

int main()
{
	int arr[1000] = { 0 };
	int test_case, temp;

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < test_case; i++)
	{
		for (int j = 0; j < test_case; j++)
		{
			if (arr[i] < arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}

	for (int i = 0; i < test_case; i++)
		printf("%d\n", arr[i]);

	return 0;
}
