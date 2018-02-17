/*
	*
	*	문제
	*	두 자연수 A와 B가 주어진다. 이 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
	*
	*	출력
	*	첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
	*
*/

#include <stdio.h>

int main()
{
	int a, b;

	scanf("%d %d", &a, &b);

	printf("%d\n", a + b);
	printf("%d\n", a - b);
	printf("%d\n", a * b);
	printf("%d\n", a / b);
	printf("%d\n", a % b);

	return 0;
}
