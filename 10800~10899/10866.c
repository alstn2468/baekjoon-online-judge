/*
	*
	*	문제
	*	정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
	*
	*	명령은 총 여덟 가지이다.
	*	push_front X: 정수 X를 덱의 앞에 넣는다.
	*	push_back X: 정수 X를 덱의 뒤에 넣는다.
	*	pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*	pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*	size: 덱에 들어있는 정수의 개수를 출력한다.
	*	empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
	*	front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*	back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*
	*	입력
	*	첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
	*	둘쨰 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
	*	주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
	*
	*	출력
	*	출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
	*
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

typedef int Data;

typedef struct _node
{
	struct _node *next;
	struct _node *prev;
	Data data;
} Node;

typedef struct _deque
{
	Node *head;
	Node *tail;
	int size;
} Deque;

int Deque_Size(Deque *pDeq);
int Deque_Is_Empty(Deque *pDeq);
void Deque_Init(Deque *pDeq);
void Push_Front(Deque *pDeq, Data data);
void Push_Back(Deque *pDeq, Data data);
void Pop_Front(Deque*pDeq);
void Pop_Back(Deque *pDeq);
Data Deque_Front(Deque *pDeq);
Data Deque_Back(Deque *pDeq);

int main()
{
	Deque deq;
	int test_case, input;
	char oper_input[11];

	Deque_Init(&deq);

	scanf("%d", &test_case);

	while (test_case--)
	{
		scanf("%s", oper_input);

		if (!strcmp(oper_input, "push_front"))
		{
			scanf("%d", &input);

			Push_Front(&deq, input);
		}
		else if (!strcmp(oper_input, "push_back"))
		{
			scanf("%d", &input);

			Push_Back(&deq, input);
		}
		else if (!strcmp(oper_input, "pop_front"))
			Pop_Front(&deq);
		else if (!strcmp(oper_input, "pop_back"))
			Pop_Back(&deq);
		else if (!strcmp(oper_input, "size"))
			printf("%d\n", Deque_Size(&deq));
		else if (!strcmp(oper_input, "empty"))
			printf("%d\n", Deque_Is_Empty(&deq));
		else if (!strcmp(oper_input, "front"))
			printf("%d\n", Deque_Front(&deq));
		else if (!strcmp(oper_input, "back"))
			printf("%d\n", Deque_Back(&deq));
		else
			printf("OPERATOR INPUT ERROR!\n");
	}

	return 0;
}

int Deque_Size(Deque *pDeq)
{
	return pDeq->size;
}

int Deque_Is_Empty(Deque *pDeq)
{
	return pDeq->size == 0 ? TRUE : FALSE;
}

void Deque_Init(Deque *pDeq)
{
	pDeq->head = NULL;
	pDeq->tail = NULL;
	pDeq->size = 0;
}

void Push_Front(Deque *pDeq, Data data)
{
	Node *newNode = (Node *)malloc(sizeof(Node));
	newNode->data = data;

	if (Deque_Is_Empty(pDeq))
		pDeq->tail = newNode;
	else
		pDeq->head->prev = newNode;

	newNode->next = pDeq->head;
	pDeq->head = newNode;
	pDeq->size++;
}

void Push_Back(Deque *pDeq, Data data)
{
	Node *newNode = (Node *)malloc(sizeof(Node));
	newNode->data = data;

	if (Deque_Is_Empty(pDeq))
		pDeq->head = newNode;
	else
		pDeq->tail->next = newNode;

	newNode->prev = pDeq->tail;
	pDeq->tail = newNode;
	pDeq->size++;
}

void Pop_Front(Deque *pDeq)
{
	if (pDeq->size == 0)
		printf("%d\n", -1);
	else
	{
		Node *rem_deq;
		int rem_data = pDeq->head->data;

		rem_deq = pDeq->head;
		pDeq->head = pDeq->head->next;
		free(rem_deq);
		pDeq->size--;

		printf("%d\n", rem_data);

		if (pDeq->size == 0)
			pDeq->head = NULL;
	}
}

void Pop_Back(Deque *pDeq)
{
	if (pDeq->size == 0)
		printf("%d\n", -1);
	else
	{
		Node *rem_deq;
		int rem_data = pDeq->tail->data;

		rem_deq = pDeq->tail;
		pDeq->tail = pDeq->tail->prev;
		free(rem_deq);
		pDeq->size--;

		printf("%d\n", rem_data);

		if (pDeq->size == 0)
			pDeq->tail = NULL;
	}
}

Data Deque_Front(Deque *pDeq)
{
	return Deque_Is_Empty(pDeq) ? -1 : pDeq->head->data;
}

Data Deque_Back(Deque *pDeq)
{
	return Deque_Is_Empty(pDeq) ? -1 : pDeq->tail->data;
}
