
# 문제
# RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다.
# 또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다.
# 집 i의 이웃은 집 i-1과 집 i+1이다. 처음 집과 마지막 집은 이웃이 아니다.
# 각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용,
# 파랑으로 드는 비용이 주어질 때, 모든 집을 칠할 때 드는 비용의
# 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 수 N이 주어진다. N은 1,000보다 작거나 같다.
# 둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때,
# 초록으로 칠할 때, 파랑으로 칠할 때 드는 비용이 주어진다.
# 비용은 1,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.

matrix=[]
N=int(input())

for i in range(N) :
	matrix.append([0, 0, 0])

for i in range(N):
	if i == 0 :
		matrix[0] = list(map(int, input().split()))

	else :
		r, g, b = map(int, input().split())

		if r + matrix[i - 1][1] > r + matrix[i - 1][2] :
			matrix[i][0] = r + matrix[i - 1][2]

		else :
			matrix[i][0] = r + matrix[i - 1][1]

		if g + matrix[i - 1][0] > g + matrix[i - 1][2] :
			matrix[i][1] = g + matrix[i - 1][2]

		else :
			matrix[i][1] = g + matrix[i - 1][0]

		if b + matrix[i - 1][0] > b + matrix[i - 1][1]:
			matrix[i][2] = b +matrix[i - 1][1]

		else:
			matrix[i][2] = b + matrix[i - 1][0]

print(min(matrix[N - 1]))
