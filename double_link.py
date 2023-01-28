class CDLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, nodevalue):
        newnode = CDLLNode(nodevalue)
        self.head = newnode
        self.tail = newnode
        newnode.next = newnode
        newnode.prev = newnode
        return "CDLL is succesfully created"

    def insertNode(self, nodevalue, loc):
        if self.head == None:
            return "CDLL doesn't exist"
        else:
            newnode = CDLLNode(nodevalue)
            if loc == 0:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head = newnode
                self.head.next.prev = newnode
                self.head.prev.next = newnode
            elif loc == 1:
                newnode.prev = self.tail
                newnode.next = self.head
                self.tail = newnode
                self.tail.prev.next = newnode
                self.head.prev = newnode
            return "Node {} inserted".format(nodevalue)




Cdllist = CDLinkList()
print(Cdllist.createCDLL(9))
print(Cdllist.insertNode(1,0))
print(Cdllist.insertNode(4,1))
print([i.value for i in Cdllist])



