/*
	*
	*	문제
	*	정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
	*	명령은 총 다섯 가지이다.
	*	▶ push X: 정수 X를 스택에 넣는 연산이다.
	*	▶ pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*	▶ size: 스택에 들어있는 정수의 개수를 출력한다.
	*	▶ empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
	*	▶ top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	*
	*	입력
	*	첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
	*	주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
	*
	*	출력
	*	출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
	*
*/

#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
#define STACK_LEN 10000

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
} ArrayStack;

typedef ArrayStack Stack;

/* 정수 data를 스택에 넣는 함수 */
void Stack_Push(Stack * pstack, Data data);
/* 스택을 초기화 하는 함수 */
void Stack_Init(Stack * pstack);
/* 스택이 가득 찼다면 TRUE 아니면 FALSE를 반환하는 함수 */
int Stack_Is_Full(Stack * pstack);
/* 스택의 가장 위의 정수를 뺀 후 출력하는 함수, 값이 없으면 -1 */
int Stack_Pop(Stack * pstack);
/* 스택에 저장되어 있는 데이터의 개수를 출력하는 함수 */
int Stack_Size(Stack * pstack);
/* 스택이 비어있으면 TRUE 아니면 FALSE 반환 */
int Stack_Is_Empty(Stack * pstack);
/* 스택의 가장 위의 정수를 출력하는 함수, 값이 없으면 -1 */
int Stack_Top(Stack * pstack);

int main()
{
	Stack stack;

	Stack_Init(&stack);

	int test_case;
	char func_input[6];
	int input_num;

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++)
	{
		scanf("%s", &func_input);

		if (!strcmp(func_input, "push"))
		{
			scanf("%d", &input_num);
			getchar();
			Stack_Push(&stack, input_num);
		}
		else if (!strcmp(func_input, "pop"))
			printf("%d\n", Stack_Pop(&stack));
		else if (!strcmp(func_input, "size"))
			printf("%d\n", Stack_Size(&stack));
		else if (!strcmp(func_input, "empty"))
			printf("%d\n", Stack_Is_Empty(&stack));
		else if (!strcmp(func_input, "top"))
			printf("%d\n", Stack_Top(&stack));
		else
			printf("Function Input Error!\n");
	}

	return 0;
}

/* 정수 data를 스택에 넣는 함수 */
void Stack_Push(Stack * pstack, Data data)
{
	if (Stack_Is_Full(pstack) == TRUE)
		return;
	else
		pstack->stackArr[++(pstack->topIndex)] = data;
}

/* 스택을 초기화 하는 함수 */
void Stack_Init(Stack * pstack)
{
	pstack->topIndex = -1;
}

/* 스택이 가득 찼다면 TRUE 아니면 FALSE를 반환하는 함수 */
int Stack_Is_Full(Stack * pstack)
{
	if (pstack->topIndex + 1 >= STACK_LEN)
		return TRUE;
	else
		return FALSE;
}

/* 스택의 가장 위의 정수를 뺀 후 출력하는 함수, 값이 없으면 -1 */
int Stack_Pop(Stack * pstack)
{
	if (Stack_Is_Empty(pstack) == TRUE)
		return -1;
	else
		return pstack->stackArr[(pstack->topIndex)--];
}

/* 스택에 저장되어 있는 데이터의 개수를 출력하는 함수 */
int Stack_Size(Stack * pstack)
{
	return pstack->topIndex + 1;
}

/* 스택이 비어있으면 TRUE 아니면 FALSE 반환 */
int Stack_Is_Empty(Stack * pstack)
{
	if (pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

/* 스택의 가장 위의 정수를 출력하는 함수, 값이 없으면 -1 */
int Stack_Top(Stack * pstack)
{
	if (Stack_Is_Empty(pstack) == TRUE)
		return -1;
	else
		return pstack->stackArr[pstack->topIndex];
}
