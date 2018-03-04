/*
	*
	*	문제
	*	다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
	*	다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다.
	*	한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
	*	다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오.
	*	(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
	*
	*	입력
	*	첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.
	*
	*	출력
	*	첫째 줄에 필요한 세트의 개수를 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char input[7] = { 0 };
	int num_count[10] = { 0 };
	int max = 0, Sum_6_9 = 0;

	scanf("%s", &input);

	for (int i = 0; i < strlen(input); i++)
	{
		num_count[input[i] - '0']++;
	}

	for (int i = 0; i < sizeof(num_count) / sizeof(int); i++)
	{
		if (i == 6 || i == 9)
			continue;
		else
		{
			if (num_count[i] > max)
				max = num_count[i];
		}
	}

	Sum_6_9 = num_count[6] + num_count[9];

	if (Sum_6_9 <= max * 2)
	{
		printf("%d\n", max);
	}
	else
	{
		if (Sum_6_9 % 2 == 1)
			printf("%d\n", Sum_6_9 / 2 + 1);
		else
			printf("%d\n", Sum_6_9 / 2);
	}

	return 0;
}																				
