/*
	*
	*	문제
	*	M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1≤M≤N≤1,000,000)
	*
	*	출력
	*	한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
	*
*/

#include<stdio.h>

int main()
{
	int num1, num2;

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
			printf("%d\n", i);
		}
	}

	return 0;
}
