/*
	*
	*	문제
	*	어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
	*	등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
	*	N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
	*
	*	출력
	*	첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
	*
*/

#include <stdio.h>

int count = 0;

void sol(int i);

int main()
{
	int input_num;

	scanf("%d", &input_num);

	for (int i = 1; i <= input_num; i++)
		sol(i);

	printf("%d\n", count);

	return 0;
}

void sol(int i)
{
	if (i < 100)
		count++;
	else if (i < 1000)
	{
		int hund_place = i / 100;
		int ten_place = (i % 100) / 10;
		int unit_place = (i % 100) % 10;

		if (hund_place - ten_place == ten_place - unit_place)
			count++;
	}
}
