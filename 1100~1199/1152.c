/*
	*
	*	문제
	*	영어 대소문자와 띄어쓰기만으로 이루어진 문장이 주어진다. 이 문장에는 몇 개의 단어가 있을까?
	*	이를 구하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문장이 주어진다. 이 문장의 길이는 1,000,000을 넘지 않는다.
	*	단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.
	*
	*	출력
	*	첫째 줄에 단어의 개수를 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char input;
	int count = 0;
	int check = 1;

	while ((input = getchar()) != EOF && input != '\n')
	{
		if (input == ' ')
		{
			check = 1;
		}
		else
		{
			if (check != 0)
			{
				count++;
				check = 0;
			}
		}
	}

	printf("%d\n", count);

	return 0;
}
