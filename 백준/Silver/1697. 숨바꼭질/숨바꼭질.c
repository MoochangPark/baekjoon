#include <stdio.h>
#define SIZE 100010

int N = 0, M = 0;

int vertex[200001];

struct queue_check
{
	int point;
	int walking;
};

struct queue_check queue[SIZE];

int BFS(int n)
{
	int front = 0, rear = 0;
	int f_vertex = 0;
	int walking_check = 0;
	int i = 0, j = 0;

	rear = (rear + 1) % SIZE;
	queue[rear].point = n;
	queue[rear].walking = 0;

	vertex[n] = 1;

	while (front != rear)
	{
		front = (front + 1) % SIZE;
		f_vertex = queue[front].point;
		walking_check = queue[front].walking;

		if (f_vertex == M)
			break;

		if ((f_vertex - 1) >= 0 && vertex[f_vertex - 1] == 0)
		{
			rear = (rear + 1) % SIZE;
			queue[rear].point = f_vertex - 1;
			queue[rear].walking = walking_check + 1;

			vertex[f_vertex - 1] = 1;
		}

		if ((f_vertex + 1) <= 200001 && vertex[f_vertex + 1] == 0)
		{
			rear = (rear + 1) % SIZE;
			queue[rear].point = f_vertex + 1;
			queue[rear].walking = walking_check + 1;

			vertex[f_vertex + 1] = 1;
		}

		if ((2 * f_vertex) <= 200001 && vertex[2 * f_vertex] == 0)
		{
			rear = (rear + 1) % SIZE;
			queue[rear].point = (2 * f_vertex);
			queue[rear].walking = walking_check + 1;

			vertex[2 * f_vertex] = 1;
		}
	}
	return walking_check;
}

int main()
{
	int i = 0, j = 0;

	scanf("%d %d", &N, &M);

	printf("%d", BFS(N));

	return 0;
}