/*
	*
	*	문제
	*	알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
	*		1. 길이가 짧은 것부터
	*		2. 길이가 같으면 사전 순으로
	*
	*	입력
	*	첫째 줄에 단어의 개수 N이 주어진다.
	*	(1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
	*	주어지는 문자열의 길이는 50을 넘지 않는다.
	*
	*	출력
	*	조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

struct word_
{
	char word[51];
	int str_len;
};

int compare(struct word_ *a, struct word_ *b);

int main()
{
	int test_case;

	struct word_ Word[20001];

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%s", Word[i].word);
		Word[i].str_len = strlen(Word[i].word);
	}

	qsort(Word, test_case, sizeof(struct word_), compare);

	int temp = 0;

	for (int i = 1; i <= test_case; i++)
	{
		if (strcmp(Word[temp].word, Word[i].word))
		{
			printf("%s\n", Word[temp].word);
			temp = i;
		}
	}

	return 0;
}

int compare(struct word_ *a, struct word_ *b)
{
	return a->str_len > b->str_len ? 1 : a->str_len < b->str_len ? -1 : strcmp(a->word, b->word);
}
