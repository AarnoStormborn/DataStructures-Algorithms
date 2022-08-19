from dataclasses import dataclass
import numpy as np

@dataclass
class Node:
    data: int = None
    next: int = None
    
@dataclass
class Stack:
    head: int = None

    def length(self):
        if self.head == None: return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def pushList(self, dataList):
        for data in dataList:
            self.push(data)

    def pop(self):
        if self.head == None: return
        item = self.head.data
        self.head = self.head.next
        return item
        
    def isEmpty(self):
        if self.head == None: return True
        return False

    def printStack(self):
        if self.head == None: return
        stk = ""
        itr = self.head
        while itr:
            stk += str(itr.data) + " "
            itr = itr.next
        return stk

# Driver code
if __name__=='__main__':
    s = Stack()

    n = int(input("Enter size of stack: "))

    inp = np.random.randint(1, 100, n)
    s.pushList(inp)
    print(s.printStack())