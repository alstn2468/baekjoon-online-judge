/*
	*
	*	문제
	*	주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
	*
	*	출력
	*	주어진 수들 중 소수의 개수를 출력한다.
	*
*/

#include<stdio.h>

int main()
{
	int test_case, check = 0, count = 0;
	int arr[101] = { 0 };

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%d", &arr[i]);

		if (arr[i] == 2)
			count++;
		else if (arr[i] == 1)
			continue;
		else
		{
			for (int j = 2; j * j <= arr[i]; j++)
			{
				if (arr[i] % j == 0)
				{
					check = -1;
					break;
				}
			}
			if (check != -1)
			{
				count++;
			}
			check = 0;
		}
	}

	printf("%d", count);

	return 0;
}
