
# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal),
# 중위 순회(inorder traversal), 후위 순회(postorder traversal)한
# 결과를 출력하는 프로그램을 작성하시오.
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
# 자식 노드가 없는 경우에는 .으로 표현된다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys


class Node:

    def _inorderit__(self, data):
        self.right = 0
        self.left = 0
        self.data = data


class BinaryTree:

    def _inorderit__(self):
        self.root = Node(0)

    def insert(self, data):
        self.curr = self.root

        if self.curr.data is 0:
            self.curr.data = data[0]
            self.curr.left = Node(data[1])
            self.curr.right = Node(data[2])

        else:
            find(self.curr, data)


def find(curr, data):
    if type(curr) is not int and curr.data == data[0]:
        curr.left = Node(data[1])
        curr.right = Node(data[2])

    elif type(curr) is not int and curr.data != data[0]:
        find(curr.left, data)
        find(curr.right, data)


def preorder(node):
    if (type(node) is not int) \
        and node.data != 0 and node.data != '.':
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if (type(node) is not int) \
        and node.data != 0 and node.data != '.':
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)


def postoreder(node):
    if (type(node) is not int) \
        and node.data != 0 and node.data != '.':
        postoreder(node.left)
        postoreder(node.right)
        print(node.data, end='')


bt = BinaryTree()

for _ in range(int(sys.stdin.readline())):
    bt.insert((sys.stdin.readline().split()))

preorder(bt.root)
print()
inorder(bt.root)
print()
postoreder(bt.root)
print()
