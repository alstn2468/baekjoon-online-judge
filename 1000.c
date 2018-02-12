/*
	*
	*	문제
	*	두 수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 A와 B가 주어진다. (0 < A,B < 10)
	*
	*	출력
	*	첫째 줄에 A+B를 출력한다.
	*
*/

#include <stdio.h>

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a + b);

	return 0;
}
