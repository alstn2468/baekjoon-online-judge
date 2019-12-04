
# 문제
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
#
# 출력
# 첫째 줄에 0의 개수를 출력한다.

def count_base(number, b):
    cnt, i = 0, b

    while number // i:
        cnt += (number // i)
        i *= b

    return cnt

n, m = map(int, input().split())

five_cnt = count_base(n, 5) - count_base(n - m, 5) - count_base(m, 5)
two_cnt = count_base(n, 2) - count_base(n - m, 2) - count_base(m, 2)
print(min(five_cnt, two_cnt))
