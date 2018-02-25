/*
	*
	*	문제
	*	상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
	*	전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
	*	다른 숫자를 누르려면 다이얼이 원래 위치로 돌아가기를 기다려야 한다.
	*	숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
	*	상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
	*	즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
	*	할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 시간을 구하는 프로그램을 작성하시오.
	*	두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*	첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.
	*
	*	출력
	*	첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

int Solution(char C)
{
	if (C == 'A' || C == 'B' || C == 'C')
		return 2;
	else if (C == 'D' || C == 'E' || C == 'F')
		return 3;
	else if (C == 'G' || C == 'H' || C == 'I')
		return 4;
	else if (C == 'J' || C == 'K' || C == 'L')
		return 5;
	else if (C == 'M' || C == 'N' || C == 'O')
		return 6;
	else if (C == 'P' || C == 'Q' || C == 'R' || C == 'S')
		return 7;
	else if (C == 'T' || C == 'U' || C == 'V')
		return 8;
	else if (C == 'W' || C == 'X' || C == 'Y' || C == 'Z')
		return 9;
	else
		return 0;
}

int main()
{
	char input[16];
	int num;
	int total_time = 0;
	int i;

	scanf("%s", input);

	for (i = 0; i < strlen(input); i++)
	{
		num = Solution(input[i]);
		total_time += (num + 1);
	}

	printf("%d\n", total_time);

	return 0;
}
