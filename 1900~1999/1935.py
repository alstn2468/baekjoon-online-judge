# 문제
# 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다.
# 그리고 둘째 줄에는 후위 표기식이 주어진다.
# (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다)
# 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.
# (3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 ,
# 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 정수이다)
#
# 출력
# 계산 결과를 소숫점 둘째 자리까지 출력한다.

N = int(input())
postfix = input()
alp, stack = [0 for _ in range(N)], []

for i in range(N):
    alp[i] = int(input())

for c in postfix:
    if "A" <= c <= "Z":
        stack.append(alp[ord(c) - ord("A")])

    else:
        b = stack.pop()
        a = stack.pop()

        if c == "+":
            stack.append(a + b)

        elif c == "-":
            stack.append(a - b)

        elif c == "/":
            stack.append(a / b)

        elif c == "*":
            stack.append(a * b)

print(f"{stack[0]:.2f}")
