
# 문제
# e는
# 이다. 여기서 n은 무한대이다.
# 매우 작은 n에 대해서, e의 근사값을 구해보자.
# 
# 출력
# 아래 결과와 같은 형식으로 e의 근사값을 n = 0부터 9까지 출력한다. 

print("n e")
print("- -----------")
print("0 1")
print("1 2")
print("2 2.5")

ret, fact = 2.5, 2

for i in range(3, 10):
    fact *= i
    ret += 1.0 / fact
    
    print("%d %.9f" % (i, ret))
