/*
	*
	*	문제
	*	A+B를 계산하시오.
	*
	*	입력
	*	첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)
	*
	*	출력
	*	첫째 줄에 A+B를 출력한다. (A+B < 10)
	*
*/

#include <stdio.h>

int main()
{
	int a, b;

	scanf("%d", &a);
	scanf("%d", &b);

	printf("%d", a + b);

	return 0;
}
