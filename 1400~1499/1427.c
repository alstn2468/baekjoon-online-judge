/*
	*
	*	문제
	*	배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
	*
	*	입력
	*	첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
	*
	*	출력
	*	첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int Bubble_Sort(char arr[], int n)
{
	char temp;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arr[i] < arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}

int main()
{
	char input[11];

	scanf("%s", &input);

	int str_len = strlen(input);

	Bubble_Sort(input, str_len);

	for (int i = str_len - 1; i >= 0; i--)
		printf("%c", input[i]);

	return 0;
}
