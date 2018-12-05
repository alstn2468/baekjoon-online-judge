
# 문제
# 시작 -> 실행 -> cmd를 쳐보자. 검정 화면이 눈에 보인다.
# 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다.
# 이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.
# dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다.
# "dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다.
# 예를 들어, dir a?b.exe라고 검색하면 파일명의 첫 번째 글자가 a이고,
# 세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다.
# 이때 두 번째 문자는 아무거나 나와도 된다. 예를 들어, acb.exe, aab.exe, apb.exe가 나온다.
# 이 문제는 검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다.
# 패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다.
# 그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.
#
# 입력
# 첫째 줄에 파일 이름의 개수 N이 주어진다.
# 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다.
# N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다.
# 파일이름은 알파벳과 "." 그리고 "?"로만 이루어져 있다.
#
# 출력
# 첫째 줄에 패턴을 출력하면 된다.

import sys

n = int(sys.stdin.readline().strip())
file_name = []

for _ in range(n):
    file_name.append(sys.stdin.readline().strip())

if n != 1 :
    length = len(file_name[0])
    pattern = [0] * length

    for i in range(n - 1):
        for j in range(length):
            if file_name[i][j] is file_name[i + 1][j] \
                and pattern[j] is not '?':
                pattern[j] = file_name[i][j]

            else:
                pattern[j] = '?'

    print(''.join(pattern))

else:
    print(file_name[0])
