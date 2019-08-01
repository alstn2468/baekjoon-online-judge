
# 문제
# 체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 
# 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. 
# ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.
# 
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

chess_board = [list(input()) for _ in range(8)]
result = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if chess_board[i][j] == 'F':
                result += 1
        
    else:
        for j in range(1, 8, 2):
            if chess_board[i][j] == 'F':
                result += 1
                
print(result)
