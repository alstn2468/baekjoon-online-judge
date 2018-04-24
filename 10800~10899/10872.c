/*
	*
	*	문제
	*	0보다 크거나 같은 정수 N이 주어진다. 이 때, N!을 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
	*
	*	출력
	*	첫째 줄에 N!을 출력한다.
	*
*/

#include <stdio.h>

int iter_factorial(int input)
{
	int result = 1;

	for (int i = input; i > 0; i--)
		result *= i;

	return result;
}

int main()
{
	int input;

	scanf("%d", &input);

	printf("%d\n", iter_factorial(input));

	return 0;
}
