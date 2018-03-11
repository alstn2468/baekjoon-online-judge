/*
	*
	*	문제
	*	M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
	*
	*	출력
	*	한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
	*
*/

#include <stdio.h>

#define MAX 1000001

int main()
{
	int num1, num2;
	int arr[MAX] = { 0,1 };

	scanf("%d %d", &num1, &num2);

	for (int i = 2; i <= num2; i++)
	{
		for (int j = 2; i * j <= num2; j++)
			arr[i * j] = 1;
	}

	for (int i = num1; i <= num2; i++)
	{
		if (!arr[i])
			printf("%d\n", i);
	}

	return 0;
}
