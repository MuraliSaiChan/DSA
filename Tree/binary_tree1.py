class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        temp = self.queue[0]
        del self.queue[0]
        return temp

    def show(self):
        print({i:j for i,j in enumerate(self.queue)})

    def empty(self):
        return len(self.queue) == 0


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def preorder(self,root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def levelorder(self,root):
        if root is None:
            return
        else:
            q = Queue()
            q.enqueue(root)
            while not q.empty():
                root = q.dequeue()
                print(root.value)
                if root.left is not None:
                    q.enqueue(root.left)
                if root.right is not None:
                    q.enqueue(root.right)





a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

t = Tree()
t.levelorder(a)



