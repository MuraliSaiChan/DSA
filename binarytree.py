import QueueLL as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


tree = TreeNode("Suribabu")
murali = TreeNode("Murali")
Lakshmi = TreeNode("lakshmi")
ch1 = TreeNode("ch1")
ch2 = TreeNode("ch2")
Lakshmi.left = ch1
Lakshmi.right = ch2
tree.left = murali
tree.right = Lakshmi


def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.left)
    preorder(rootnode.right)

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.left)
    print(rootnode.data)
    inorder(rootnode.right)

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.left)
    postorder(rootnode.right)
    print(rootnode.data)

def LevelOrder(rootnode):
    if not rootnode:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootnode)
        while not q.isEmpty():
            temp = q.dequeue()
            if temp.value.left is not None:
                q.enqueue(temp.value.left)
            if temp.value.right is not None:
                q.enqueue(temp.value.right)
            print(temp.value.data)

def insertNode(rootnode, data):
    if not rootnode:
        return
    newnode = TreeNode(data)
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isEmpty():
        root = q.dequeue()
        if root.value.left is not None:
            q.enqueue(root.value.left)
        else:
            root.value.left = newnode
            print("succesfully inserted")
            return

        if root.value.right is not None:
            q.enqueue(root.value.right)
        else:
            root.value.right = newnode
            print("succesfully inserted")
            return

def deleteNode(root,data):
    if root is None:
        return



preorder(tree)
print("inorder")
inorder(tree)
print("postorder")
postorder(tree)
print("levelorder")
LevelOrder(tree)

insertNode(tree, "m1")
insertNode(tree, "m2")
insertNode(tree, "m3")
insertNode(tree, "m4")
insertNode(tree, "m5")
insertNode(tree, "m6")
insertNode(tree, "m7")
insertNode(tree, "m8")
insertNode(tree, "m9")
insertNode(tree, "m10")
LevelOrder(tree)

print(lastnode(tree))
#preorder(tree)