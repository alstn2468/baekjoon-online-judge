/*
	*
	*	문제
	*	그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
	*	단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
	*	더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
	*
	*	입력
	*	첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
	*	다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
	*	한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.
	*
	*	출력
	*	첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
	*
*/

#include <stdio.h>

int Vertex_Count, Edge;
int map[1001][1001];
int visit_DFS[1001];
int visit_BFS[1001];
int queue[1001];
int rear, front;

void DFS(int Vertex)
{
	visit_DFS[Vertex] = 1;
	printf("%d ", Vertex);

	for (int i = 1; i <= Vertex_Count; i++)
	{
		if (map[Vertex][i] == 1 && !visit_DFS[i])
		{
			visit_DFS[i] = 1;
			DFS(i);
		}
	}
}

void BFS(int Vertex)
{
	visit_BFS[Vertex] = 1;
	queue[rear++] = Vertex;

	while (front < rear)
	{
		Vertex = queue[front++];
		printf("%d ", Vertex);

		for (int i = 1; i <= Vertex_Count; i++)
		{
			if (map[Vertex][i] == 1 && !visit_BFS[i])
			{
				visit_BFS[i] = 1;
				queue[rear++] = i;
			}
		}
	}
}

int main()
{
	int Vertex_1, Vertex_2;
	int start;

	scanf("%d %d %d", &Vertex_Count, &Edge, &start);

	for (int i = 1; i <= Edge; i++)
	{
		scanf("%d %d", &Vertex_1, &Vertex_2);
		map[Vertex_1][Vertex_2] = map[Vertex_2][Vertex_1] = 1;
	}

	DFS(start);
	printf("\n");
	BFS(start);

	return 0;
}
