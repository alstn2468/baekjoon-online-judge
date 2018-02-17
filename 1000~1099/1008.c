/*
	*
	*	문제
	*	A/B를 계산하시오.
	*
	*	입력
	*	첫째 줄에 A와 B가 주어진다. (0 < A,B < 10)
	*
	*	출력
	*	첫째 줄에 A/B를 출력한다. 절대/상대 오차는 10-9 까지 허용한다.
	*
*/

#include <stdio.h>

int main()
{
	double a, b;

	scanf("%lf %lf", &a, &b);

	printf("%.9f", a / b);

	return 0;
}
