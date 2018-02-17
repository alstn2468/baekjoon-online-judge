/*
	*
	*	문제
	*	조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
	*	이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
	*	조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
	*	류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
	*
	*	입력
	*
	*	첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.
	*	한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고,
	*	10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
	*
	*	출력
	*	각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다.
	*	만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
	*
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct circle
{
	double xpos;
	double ypos;
	double radius;
}circle;

double Get_Distance(double x1, double y1, double x2, double y2);
int Get_Num_Of_Node(circle cir1, circle cir2);

int main(void)
{
	int t_case;
	int *arr;
	scanf("%d", &t_case);
	arr = (int*)malloc(sizeof(int)*t_case);

	circle cir1, cir2;

	for (int i = 0; i < t_case; i++)
	{
		scanf("%lf %lf %lf %lf %lf %lf", &cir1.xpos, &cir1.ypos, &cir1.radius, &cir2.xpos, &cir2.ypos, &cir2.radius);

		arr[i] = Get_Num_Of_Node(cir1, cir2);
	}

	for (int i = 0; i < t_case; i++)
	{
		printf("%d\n", arr[i]);
	}
	free(arr);

	return 0;
}

double Get_Distance(double x1, double y1, double x2, double y2)
{
	return sqrt((double)((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
}

int Get_Num_Of_Node(circle cir1, circle cir2)
{
	int numOfnode;
	double distance = Get_Distance(cir1.xpos, cir1.ypos, cir2.xpos, cir2.ypos);

	/* 교점 없음 */
	if (abs(cir1.radius - cir2.radius) > distance)
	{
		numOfnode = 0;
	}

	/* 교점 1개(두 원이 내접함) || 교점 무한개 */
	else if (abs(cir1.radius - cir2.radius) == distance)
	{
		numOfnode = 1;
		if (cir1.radius == cir2.radius)
		{
			numOfnode = -1;
		}
	}

	/* 교점 2개 */
	else if (abs(cir1.radius - cir2.radius) < distance && distance < (cir1.radius + cir2.radius))
	{
		numOfnode = 2;
	}

	/* 교점 1개(두 원이 외접함) */
	else if (distance == (cir1.radius + cir2.radius))
	{
		numOfnode = 1;
	}

	/* 교점 없음 */
	else if (distance >(cir1.radius + cir2.radius))
	{
		numOfnode = 0;
	}

	return numOfnode;
}
