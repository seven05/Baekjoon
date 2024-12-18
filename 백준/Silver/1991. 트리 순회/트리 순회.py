import sys

N = int(sys.stdin.readline().strip())
tree = {}
for i in range(N):
    root,left,right = sys.stdin.readline().split()
    tree[root] = (left,right)
# print(tree)

def preorder(node):     # 전위 순회
    if node != '.':
        print(node,end="")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):      # 중위 순회
    if node != '.':
        inorder(tree[node][0])
        print(node,end="")
        inorder(tree[node][1])

def postorder(node):    # 후위 순회
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')