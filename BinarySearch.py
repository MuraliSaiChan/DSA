from QueueLL import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(rootNode, nodevalue):
    if rootNode is None:
        rootNode.data = nodevalue
    elif nodevalue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = Node(nodevalue)
        else:
            insertNode(rootNode.left, nodevalue)
    else:
        if rootNode.right is None:
            rootNode.right = Node(nodevalue)
        else:
            insertNode(rootNode.right, nodevalue)
    return "node sucesfully inserted"


def preorder(rootnode):
    if rootnode is None:
        return "No Tree"
    else:
        print(rootnode.data)
        preorder(rootnode.left)
        preorder(rootnode.right)


def inorder(rootnode):
    if rootnode is None:
        return "No Tree"
    else:
        inorder(rootnode.left)
        print(rootnode.data)
        inorder(rootnode.right)


def postorder(rootnode):
    if rootnode is None:
        return "No Tree"
    else:
        postorder(rootnode.left)
        postorder(rootnode.right)
        print(rootnode.data)


def levelorder(rootnode):
    q = Queue()
    q.enqueue(rootnode)
    while not q.isEmpty():
        temp = q.dequeue()
        print(temp.value.data)
        if temp.value.left is not None:
            q.enqueue(temp.value.left)
        if temp.value.right is not None:
            q.enqueue(temp.value.right)


# def levelorderlist(rootnode):
#     l = [rootnode]
#     while l is not []:
#         temp = l[0]
#         del l[0]
#         print(temp.data)
#         if temp.left is not None:
#             l.append(temp.left)
#         if temp.right is not None:
#             l.append(temp.right)


def minValueNode(bstNode):
    current = bstNode
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = deleteNode(root.left, value)
    elif value > root.data:
        root.right = deleteNode(root.right, value)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        if root.left is None:
            temp = root.right
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

root = Node(45)
print(insertNode(root, 50))
print(insertNode(root, 42))
print(insertNode(root, 20))
print(insertNode(root, 48))
print(insertNode(root, 100))
print(insertNode(root, 45))
print(insertNode(root, 10))

print("pre")
preorder(root)
print("in")
inorder(root)
print("post")
postorder(root)
print("level")
levelorder(root)

deleteNode(root, 10)
print("level-list")
levelorder(root)

