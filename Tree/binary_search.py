from Tree import binary_tree1

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree(binary_tree1.Tree):

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

    def search(self,root,value):
        if root.value == value:
            print("Found")
            return
        elif root.value >= value and root.left is not None:
            self.search(root.left,value)
        elif root.value < value and root.right is not None:
            self.search(root.right,value)
        else:
            print("Not found")
            return

    def min_node(self,root):
        if root.left is None:
            return root
        else:
            return self.min_node(root.left)

    def deletenode(self,root,value):
        if root is None:
            return root
        elif root.value == value:
            if root.right is None or root.left is None:
                if root.right is None:
                    temp = root.left
                    root = None
                    return temp
                elif root.left is None:
                    temp = root.right
                    root = None
                    return temp
            else:
                minnode = self.min_node(root.right)
                root.value = minnode.value
                root.right = self.deletenode(root.right, minnode.value)
                return root
        elif value < root.value:
            root.left =  self.deletenode(root.left,value)
        else:
            root.right = self.deletenode(root.right, value)



a = Node(70)
b = Node(50)
c = Node(90)
d = Node(30)
e = Node(80)
f = Node(100)
g = Node(85)
h = Node(10)

tree = Tree()
tree.insert(a,b)
tree.insert(a,c)
tree.insert(a,d)
tree.insert(a,e)
tree.insert(a,f)
tree.insert(a,g)
tree.insert(a,h)

tree.search(a,30)
print(tree.levelorder(a))

tree.deletenode(a,90)

print(tree.levelorder(a))


