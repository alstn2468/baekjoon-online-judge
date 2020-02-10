# 문제
# 자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.
#
# 입력
# 자연수 A, B(0 < A, B ≤ 10)가 첫 번째 줄에 주어진다.
# 단, 두 수의 사이에는 공백이 주어지지 않는다.
# 두 수의 앞에 불필요한 0이 붙는 경우는 없다.
#
# 출력
# 첫 번째 줄에 A+B의 값을 출력한다.

n = input()

if len(n) == 2:
    print(sum(map(int, [n[0], n[1]])))

elif len(n) == 4:
    print(20)

else:
    if int(n[-1]) == 0:
        print(int(n[0]) + 10)

    else:
        print(int(n[-1]) + 10)
