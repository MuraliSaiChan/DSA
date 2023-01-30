from Tree import binary_tree1

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:

    def insert(self, root, node):
        if root is None:
            root = node
        elif node.value <= root.value:
            if root.left is not None:
                self.insert(root.left, node)
            else:
                root.left = node
        else:
            if root.right is not None:
                self.insert(root.right,node)
            else:
                root.right = node


a = Node(70)
b = Node(50)
c = Node(90)
d = Node(30)
e = Node(80)
f = Node(100)
g = Node(85)

tree = binary_tree1.Tree()
tree2 = Tree()
tree2.insert(a,b)
tree2.insert(a,c)
tree2.insert(a,d)
tree2.insert(a,e)
tree2.insert(a,f)
tree2.insert(a,g)
tree.inorder(a)


