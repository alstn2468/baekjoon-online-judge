# 문제
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
#    1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
#    2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
#    3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다.
# 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
# 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금으로 받게 된다.
# N(2 ≤ N ≤ 1,000)명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 참여하는 사람 수 N이 주어지고
# 그 다음 줄부터 N개의 줄에 사람들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
#
# 출력
# 첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.


def calculate_prize_money(dices):
    if dices[0] == dices[1] == dices[2]:
        return 10000 + dices[0] * 1000

    if dices[0] != dices[1] and dices[0] != dices[2] and dices[1] != dices[2]:
        return max(dices) * 100

    same_dice = None

    if dices[0] == dices[1]:
        same_dice = dices[0]

    elif dices[0] == dices[2]:
        same_dice = dices[0]

    elif dices[1] == dices[2]:
        same_dice = dices[1]

    return 1000 + same_dice * 100


result = []

for _ in range(int(input())):
    result.append(calculate_prize_money(list(map(int, input().split()))))

print(max(result))
