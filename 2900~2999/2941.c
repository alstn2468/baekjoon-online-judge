/*
	*
	*	문제
	*	예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 다음과 같이 변경해서 입력했다.
	*	크로아티아 알파벳	변경
	*			č			c=
	*			ć			c-
	*			dž			dz=
	*			ñ			d-
	*			lj			lj
	*			nj			nj
	*			š			s=
	*			ž			z=
	*	예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때,
	*	몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
	*	dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
	*	위 목록에 없는 알파벳은 한 글자씩 센다.
	*
	*	입력
	*	첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
	*	문제 설명에 나와있는 크로아티아 알파벳만 주어진다.
	*
	*	출력
	*	입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char input[101] = { 0 };
	int alp_num_count = 0;
	int i = 0;

	scanf("%s", &input);

	int str_len = strlen(input);

	while(i < str_len)
	{
		if (input[i] == 'c')
		{
			if (input[i + 1] == '=' || input[i + 1] == '-')
				i += 2;
			else i++;
		}
		else if (input[i] == 'd')
		{
			if (input[i + 1] == 'z')
			{
				if (input[i + 2] == '=')
					i += 3;
				else
					i++;
			}
			else if (input[i + 1] == '-')
				i += 2;
			else
				i++;
		}
		else if (input[i] == 'l')
		{
			if (input[i + 1] == 'j')
				i += 2;
			else
				i++;
		}
		else if (input[i] == 'n')
		{
			if (input[i + 1] == 'j')
				i += 2;
			else
				i++;
		}
		else if (input[i] == 's')
		{
			if (input[i + 1] == '=')
				i += 2;
			else
				i++;
		}
		else if (input[i] == 'z')
		{
			if (input[i + 1] == '=')
				i += 2;
			else
				i++;
		}
		else
			i++;

		alp_num_count++;
	}

	printf("%d\n", alp_num_count);

	return 0;
}
