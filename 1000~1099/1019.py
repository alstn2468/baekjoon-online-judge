
# 문제
# 지민이는 N쪽인 책이 한권 있다. 
# 첫 페이지는 1쪽이고, 마지막 페이지는 N쪽이다. 
# 각 숫자가 모두 몇 번이 나오는지 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 N이 주어진다. 
# N은 1,000,000,000보다 작거나 같은 자연수이다.
# 
# 출력
# 첫째 줄에 0이 총 몇 번 나오는지, 
# 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 출력한다.

def myrange(start, end, step):
    r = start
    while(r > end):
        yield r
        r //= step

def solution(start, div, count):
    for i in myrange(start, 0, 10):
        count[i % 10] += div

N = int(input())
count = [0] * 10
start = 1
div = 1

while start <= N:
    while start % 10 != 0 and start <= N:
        solution(start, div, count)
        start += 1

    if start > N:
        break

    while N % 10 != 9 and start <= N:
        solution(N, div, count)
        N -= 1

    cnt = int((N / 10) - (start / 10) + 1)
    for i in range (10):
        count[i] += cnt * div

    start = int(start / 10)
    N  = int(N / 10)
    div *= 10

print(' '.join(list(map(str, count))))
