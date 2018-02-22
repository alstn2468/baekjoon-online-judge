/*
	*
	*	문제
	*	알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
	*	단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
	*	포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
	*
	*	출력
	*	각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치,
	*	... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
	*	만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
	*	단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
	*
*/

#include <stdio.h>

int main()
{
	char input[100];
	int alp_idx[26];

	scanf("%s", &input);

	for (int i = 0; i < sizeof(alp_idx) / sizeof(int); i++)
		alp_idx[i] = -1;

	for (int i = 0; input[i] != NULL; i++)
	{
		switch (input[i])
		{
		case 'a':
			if (alp_idx[0] != -1)
				break;

			alp_idx[0] = i;
			break;
		case 'b':
			if (alp_idx[1] != -1)
				break;

			alp_idx[1] = i;
			break;
		case 'c':
			if (alp_idx[2] != -1)
				break;

			alp_idx[2] = i;
			break;
		case 'd':
			if (alp_idx[3] != -1)
				break;

			alp_idx[3] = i;
			break;
		case 'e':
			if (alp_idx[4] != -1)
				break;

			alp_idx[4] = i;
			break;
		case 'f':
			if (alp_idx[5] != -1)
				break;

			alp_idx[5] = i;
			break;
		case 'g':
			if (alp_idx[6] != -1)
				break;

			alp_idx[6] = i;
			break;
		case 'h':
			if (alp_idx[7] != -1)
				break;

			alp_idx[7] = i;
			break;
		case 'i':
			if (alp_idx[8] != -1)
				break;

			alp_idx[8] = i;
			break;
		case 'j':
			if (alp_idx[9] != -1)
				break;

			alp_idx[9] = i;
			break;
		case 'k':
			if (alp_idx[10] != -1)
				break;

			alp_idx[10] = i;
			break;
		case 'l':
			if (alp_idx[11] != -1)
				break;

			alp_idx[11] = i;
			break;
		case 'm':
			if (alp_idx[12] != -1)
				break;

			alp_idx[12] = i;
			break;
		case 'n':
			if (alp_idx[13] != -1)
				break;

			alp_idx[13] = i;
			break;
		case 'o':
			if (alp_idx[14] != -1)
				break;

			alp_idx[14] = i;
			break;
		case 'p':
			if (alp_idx[15] != -1)
				break;

			alp_idx[15] = i;
			break;
		case 'q':
			if (alp_idx[16] != -1)
				break;

			alp_idx[16] = i;
			break;
		case 'r':
			if (alp_idx[17] != -1)
				break;

			alp_idx[17] = i;
			break;
		case 's':
			if (alp_idx[18] != -1)
				break;

			alp_idx[18] = i;
			break;
		case 't':
			if (alp_idx[19] != -1)
				break;

			alp_idx[19] = i;
			break;
		case 'u':
			if (alp_idx[20] != -1)
				break;

			alp_idx[20] = i;
			break;
		case 'v':
			if (alp_idx[21] != -1)
				break;

			alp_idx[21] = i;
			break;
		case 'w':
			if (alp_idx[22] != -1)
				break;

			alp_idx[22] = i;
			break;
		case 'x':
			if (alp_idx[23] != -1)
				break;

			alp_idx[23] = i;
			break;
		case 'y':
			if (alp_idx[24] != -1)
				break;

			alp_idx[24] = i;
			break;
		case 'z':
			if (alp_idx[25] != -1)
				break;

			alp_idx[25] = i;
			break;
		}
	}

	for (int i = 0; i < sizeof(alp_idx) / sizeof(int); i++)
	{
		printf("%d ", alp_idx[i]);
	}

	printf("\n");

	return 0;
}
