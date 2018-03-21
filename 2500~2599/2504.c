/*
	*
	*   문제
	*
	*   4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
	*		1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
	*		2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
	*		3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
	*   예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다.
	*   우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
	*		1. ‘()’ 인 괄호열의 값은 2이다.
	*		2. ‘[]’ 인 괄호열의 값은 3이다.
	*		3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
	*		4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
	*		5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
	*	예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자.  ‘()[[]]’ 의 괄호값이
	*	2 + 3×3=11 이므로  ‘(()[[ ]])’의 괄호값은 2×11=22 이다.
	*	그리고  ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.
	*	여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.
	*
	*   입력
	*
	*   첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
	*
	*   출력
	*
	*   첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
	*
*/

#include<stdio.h>
#include<string.h>

int check(char a);

int main()
{
	int str_len;
	char list[40];
	char stack[40];
	int idx = 0, mul = 1, result = 0;

	scanf("%s", list);
	str_len = strlen(list);

	for (int i = 0; i < str_len; i++)
	{
		if (check(list[i]) == 1)
		{
			stack[idx++] = list[i];
			mul *= 2;

			if (check(list[i + 1]) == 2)
			{
				result += mul;
			}
		}
		else if (check(list[i]) == 3)
		{
			stack[idx++] = list[i];
			mul *= 3;

			if (check(list[i + 1]) == 4)
			{
				result += mul;
			}
		}
		else if (check(list[i]) == 2)
		{
			if (check(stack[idx - 1]) == 1)
			{
				stack[idx--] = '0';
				mul /= 2;
			}
			else
			{
				stack[idx++] = list[i];
			}
		}
		else if (check(list[i]) == 4)
		{
			if (check(stack[idx - 1]) == 3)
			{
				stack[idx--] = '0';
				mul /= 3;
			}
			else
			{
				stack[idx++] = list[i];
			}
		}
	}
	if (idx == 0)
		printf("%d\n", result);
	else
		printf("0\n");

	return 0;
}

int check(char a)
{
	if (a == '(')
		return 1;
	else if (a == ')')
		return 2;
	else if (a == '[')
		return 3;
	else if (a == ']')
		return 4;
}
