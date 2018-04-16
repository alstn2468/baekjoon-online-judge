/*
*
*	문제
*	조세퍼스 문제는 다음과 같다.
*	1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다.
*	이제 순서대로 M번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
*	이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다.
*	예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
*	N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.
*
*	입력
*	첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 5,000)
*
*	출력
*	예제와 같이 조세퍼스 순열을 출력한다.
*
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 1000
#define TRUE 1
#define FALSE 0

typedef struct _list
{
	int data;
	struct _list *next;
	struct _list *pre;
} List;

typedef struct _head
{
	List *front;
	List *rear;
	int size;
} Head;

List * Make_List(Head *phead, int num);
void Remove_List(List *plist);

int main()
{
	int N, M;

	scanf("%d %d", &N, &M);

	Head *h = (Head *)malloc(sizeof(Head));
	h->front = NULL;
	h->rear = NULL;
	h->size = 0;

	for (int i = 1; i <= N; i++)
	{
		List *plist = Make_List(h, i);
	}
	h->rear->next = h->front;
	h->front->pre = h->rear;

	printf("<");

	while (TRUE)
	{
		List *temp = h->front;

		for (int i = 0; i < M - 1; i++)
			temp = temp->next;

		if (h->size > 1)
		{
			h->front = temp->next;
			printf("%d, ", temp->data);
			Remove_List(temp);
			h->size--;
		}
		else
		{
			printf("%d", temp->data);
			Remove_List(temp);
			break;
		}
	}
	printf(">\n");

	return 0;
}

List * Make_List(Head *phead, int num)
{
	List *list = (List *)malloc(sizeof(List));
	list->data = num;
	list->next = 0;

	if (phead->front == 0)
	{
		phead->front = list;
		phead->rear = list;
		phead->size++;
	}
	else
	{
		list->pre = phead->rear;
		phead->rear->next = list;
		phead->rear = list;
		phead->size++;
	}

	return list;
}
void Remove_List(List *plist)
{
	plist->pre->next = plist->next;
	plist->next->pre = plist->pre;

	free(plist);
}
