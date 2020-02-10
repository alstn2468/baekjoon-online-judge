# 문제
# 방금 도착한 암호문을 해독했는데, 해독에 오류가 없는지 확인해보려 한다.
# 해독한 문장이 암호문을 해석한 결과로 나올 수 없다면, 그 해독은 잘못된 것이다.
# 암호문은 0 이상 52 이하의 정수로 이루어져 있다.
# 0은 띄어쓰기, 1 - 26 범위 안의 수는 A ~ Z, 27 - 52 범위 안의 수는 a ~ z로 해석된다.
# 암호문은 띄어쓰기를 포함한 모든 철자를 이와 같이 정수로 치환한 후 순서를 무작위로 뒤섞어서 만들어졌다.
#
# 입력
# 첫 번째 줄에는 주어질 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)
# 두 번째 줄에는 암호문에 해당하는 수 N개가 띄어쓰기와 함께 주어진다.
# 세 번째 줄에는 평문이 주어진다. 단, 평문의 길이는 N과 같으며, 띄어쓰기로 시작하거나 끝나지 않는다.
#
# 출력
# 평문을 암호화해서 주어진 암호문을 만들 수 있다면 "y", 아니라면 "n"을 따옴표 없이 출력한다.


def decryption(cipher):
    result = []

    for c in cipher:
        if c == 0:
            result.append(" ")

        elif 1 <= c <= 26:
            result.append(chr((c - 1) + 65))

        else:
            result.append(chr((c - 27) + 97))

    return result


N = int(input())
cipher = list(map(int, input().split()))
plain_text = sorted(input())
decryption_text = sorted(decryption(cipher))

if plain_text == decryption_text:
    print("y")

else:
    print("n")
