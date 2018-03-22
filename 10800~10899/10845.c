/*
	*
	*	문제
	*
	*	정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
	*	명령은 총 여섯 가지이다.
	*		1. push X: 정수 X를 큐에 넣는 연산이다.
	*		2. pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
	*				만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*		3. size: 큐에 들어있는 정수의 개수를 출력한다.
	*		4. empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
	*		5. front: 큐의 가장 앞에 있는 정수를 출력한다.
	*				  만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*		6. back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*
	*	입력
	*
	*	첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
	*	둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
	*	주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
	*
	*	출력
	*
	*	출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0
#define QUEUE_LEN 10000

typedef int Data;

typedef struct _queue
{
	int head;
	int tail;
	int numOfData;
	Data Q_Arr[QUEUE_LEN];
} cQueue;

typedef cQueue Q;

void Queue_Init(Q * pq);
void Set_Next_Idx(int * idx);
void Queue_Push(Q * pq, Data data);

int Get_Next_Idx(int idx);
int Queue_Is_Empty(Q * pq);
int Queue_Is_Full(Q * pq);

Data Queue_Front(Q * pq);
Data Queue_Back(Q * pq);
Data Queue_Pop(Q * pq);

int main()
{
	int test_case;
	char input[6];

	scanf("%d", &test_case);

	Q Queue;
	Data data;

	Queue_Init(&Queue);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%s", input);

		if (!strcmp(input, "push"))
		{
			scanf("%d", &data);
			Queue_Push(&Queue, data);
		}
		else if (!strcmp(input, "pop"))
			printf("%d\n", Queue_Pop(&Queue));
		else if (!strcmp(input, "size"))
			printf("%d\n", Queue.numOfData);
		else if (!strcmp(input, "empty"))
			printf("%d\n", Queue_Is_Empty(&Queue));
		else if (!strcmp(input, "front"))
			printf("%d\n", Queue_Front(&Queue));
		else if (!strcmp(input, "back"))
			printf("%d\n", Queue_Back(&Queue));
		else
			printf("INPUT ERROR!\n");
	}

	return 0;
}

void Queue_Init(Q * pq)
{
	pq->head = NULL;
	pq->numOfData = 0;
	pq->tail = NULL;
}

void Set_Next_Idx(int * idx)
{
	if (*idx + 1 >= QUEUE_LEN)
		*idx = 0;
	else
		(*idx)++;
}

void Queue_Push(Q * pq, Data data)
{
	if (Queue_Is_Full(pq) == TRUE)
		return;

	pq->Q_Arr[pq->tail] = data;
	Set_Next_Idx(&(pq->tail));
	(pq->numOfData)++;
}

int Get_Next_Idx(int idx)
{
	if (idx + 1 >= QUEUE_LEN)
		return 0;
	else
		return idx + 1;
}

int Queue_Is_Empty(Q * pq)
{
	if (pq->head == pq->tail)
		return TRUE;
	else
		return FALSE;
}

int Queue_Is_Full(Q * pq)
{
	if (Get_Next_Idx(pq->tail) == pq->head)
		return TRUE;
	else
		return FALSE;
}

Data Queue_Front(Q * pq)
{
	if (Queue_Is_Empty(pq) == TRUE)
		return -1;
	else
		return pq->Q_Arr[pq->head];
}

Data Queue_Back(Q * pq)
{
	if (Queue_Is_Empty(pq) == TRUE)
		return -1;
	else
		return pq->Q_Arr[pq->tail - 1];
}

Data Queue_Pop(Q * pq)
{
	if (Queue_Is_Empty(pq) == TRUE)
		return -1;

	Data data = pq->Q_Arr[pq->head];
	Set_Next_Idx(&(pq->head));
	(pq->numOfData)--;

	return data;
}
