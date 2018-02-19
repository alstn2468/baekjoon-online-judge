/*
	*
	*	문제
	*	예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.
	*
	*	입력
	*	첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다. (3, 6, 12, 24, 48, ...) (k<=10)
	*
	*	출력
	*	첫째 줄부터 N번째 줄까지 별을 출력한다.
	*
*/

#include <stdio.h>

void star(int n, int x, int y);

char arr[3072][6144];

int main()
{
	int n, i, j;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < 2 * n; j++)
		{
			if (j == 2 * n - 1)
				arr[i][j] = '\0';
			else
				arr[i][j] = ' ';
		}
	}

	star(n, n - 1, 0);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < 2 * n - 1; j++)
		{
			printf("%c", arr[i][j]);
		}
		printf("\n");
	}

	return 0;
}

void star(int n, int x, int y)
{
	if (n == 3)
	{
		arr[y][x] = '*';
		arr[y + 1][x - 1] = '*';
		arr[y + 1][x + 1] = '*';
		arr[y + 2][x - 2] = '*';
		arr[y + 2][x - 1] = '*';
		arr[y + 2][x] = '*';
		arr[y + 2][x + 1] = '*';
		arr[y + 2][x + 2] = '*';
		return;
	}
	star(n / 2, x, y);
	star(n / 2, x - (n / 2), y + (n / 2));
	star(n / 2, x + (n / 2), y + (n / 2));
}
