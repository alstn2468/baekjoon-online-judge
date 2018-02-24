/*
	*
	*	문제
	*	그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
	*	예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
	*	aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
	*	단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
	*	둘째줄부터 N개의 줄에 단어가 들어온다.
	*	단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
	*
	*	출력
	*	첫째 줄에 그룹 단어의 개수를 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int main()
{
	int N, i, j;
	char words[100][101];
	int cntGroupNum = 0;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
		scanf("%s", words[i]);

	for (i = 0; i < N; i++)
	{
		int cntAlphabet[26] = { 0 };
		for (j = 0; j < strlen(words[i]); j++)
		{
			if (j == 0)
				cntAlphabet[words[i][j] - 97]++;
			else
			{
				if (words[i][j] == words[i][j - 1])
				{
					if (j != strlen(words[i]) - 1)
						continue;
				}
				else
				{
					if (cntAlphabet[words[i][j] - 97] == 0)
						cntAlphabet[words[i][j] - 97]++;
					else
						break;
				}
			}

			if (j == strlen(words[i]) - 1)
				cntGroupNum++;
		}
	}

	printf("%d\n", cntGroupNum);

	return 0;
}
