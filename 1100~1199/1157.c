/*
	*
	*	문제
	*	알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
	*	단, 대문자와 소문자를 구분하지 않는다.
	*
	*	입력
	*	첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
	*	주어지는 단어의 길이는 1,000,000을 넘지 않는다.
	*
	*	출력
	*	첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
	*	단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
	*
*/

#include <stdio.h>

int main()
{
	char input[1000000] = { 0 };
	int alp_count[26] = { 0 };

	scanf("%s", &input);

	for (int i = 0; i < 1000000; i++)
	{
		if (input[i] == 0)
			break;
		for (int j = 0; j < 26; j++)
		{
			if (input[i] == j + 65 || input[i] == j + 97)
			{
				alp_count[j]++;
			}
		}
	}

	int max = 0;
	int max_index = 0;
	int same = 0;

	for (int i = 0; i < sizeof(alp_count) / sizeof(int); i++)
	{
		if (max == alp_count[i])
		{
			same += 1;
		}
		else if (max < alp_count[i])
		{
			max = alp_count[i];
			max_index = i;
			same = 0;
		}
	}

	printf("%c", same == 0 ? max_index + 65 : 63);

	return 0;
}
