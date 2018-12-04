
# 문제
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
# 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때,
# 프리오더를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n(1≤n≤100,000)이 주어진다.
# 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고,
# 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.
#
# 출력
# 첫째 줄에 프리오더를 출력한다.

def get_preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if postorder_start > postorder_end:
        return

    if inorder_start > inorder_end:
        return

    root = postorder[postorder_end]

    print(root, end=" ")

    inorder_root = inposition[root]
    left_size = inorder_root - inorder_start

    get_preorder(inorder_start, inorder_root - 1,
                 postorder_start, postorder_start + left_size - 1)
    get_preorder(inorder_root + 1, inorder_end,
                 postorder_start + left_size, postorder_end - 1)

import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split(' ')))
postorder = list(map(int, sys.stdin.readline().split(' ')))

inposition = [0] * (max(inorder) + 1)

for i, v in enumerate(inorder):
    inposition[v] = i

get_preorder(0, n - 1, 0, n - 1)
