# 문제
# 창영이는 삼각형의 종류를 잘 구분하지 못한다.
# 따라서 프로그램을 이용해 이를 외우려고 한다.
# 삼각형의 세 각을 입력받은 다음,
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.
#
# 입력
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
#
# 출력
# 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.

angles = []

for _ in range(3):
    angles.append(int(input()))

if angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
    print("Equilateral")

elif sum(angles) == 180 and (
    angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]
):
    print("Isosceles")

elif (
    sum(angles) == 180
    and angles[0] != angles[1]
    and angles[0] != angles[2]
    and angles[1] != angles[2]
):
    print("Scalene")

else:
    print("Error")
