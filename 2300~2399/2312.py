
# 문제
# 양의 정수 N이 주어졌을 때, 
# 이 수를 소인수분해 한 결과를 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 테스트 케이스의 수가 주어진다. 
# 각 테스트 케이스마다 양의 정수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 
# 출력
# 각 테스트 케이스마다 각 인수와 그 인수가 곱해진 횟수를 한 줄씩 출력한다. 
# 출력 순서는 인수가 증가하는 순으로 한다.

for _ in range(int(input())):
    N = int(input())
    result = {}
    divisor = 2
    
    while True:
        if N == 1:
            break
        
        if N % divisor == 0:
            if divisor in result.keys():
                result[divisor] += 1
                
            else:
                result[divisor] = 1
                
            N //= divisor
            
        else:
            divisor += 1
            
    for k, i in result.items():
        print(k, i)
