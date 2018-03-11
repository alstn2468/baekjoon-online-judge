/*
	*
	*	문제
	*	자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
	*	예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중
	*	소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최소값은 61이 된다.
	*
	*	입력
	*	입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
	*	M과 N은 10,000이하의 자연수이며, M은 N보다 같거나 작다.
	*
	*	출력
	*	M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최소값을 출력한다.
	*	단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
	*
*/

#include<stdio.h>

int main()
{
	int num1, num2;
	int sum = 0, count = 0, min_val = 0;

	scanf("%d", &num1);
	scanf("%d", &num2);

	if (num1 > num2)
		return 0;

	for (int i = num1; i <= num2; i++)
	{
		int check = 0;

		if (i == 1)
			check++;

		for (int j = 2; j < i; j++)
		{
			if (i % j == 0)
			{
				check++;
				break;
			}
		}

		if (check == 0)
		{
			count++;
			sum += i;

			if (count == 1)
				min_val = i;
		}
	}

	if (sum == 0)
		printf("%d", -1);
	else
	{
		printf("\n%d\n", sum);
		printf("%d\n", min_val);
	}

	return 0;
}
