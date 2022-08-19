from dataclasses import dataclass

@dataclass
class Node:
    data: int = None
    next: int = None

@dataclass
class LinkedList:
    head: int = None

    def getLength(self):
        if self.head == None: return
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertEnd(self, data):
        if self.head == None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insertStart(self, data):
        if self.head == None:
            node = Node(data, None)
            self.head = node
            return
        
        node = Node(data, self.head)
        self.head = node

    def insertList(self, dataList):
        for data in dataList:
            self.insertEnd(data)
        
    def removeEnd(self):
        if self.head == None: return "List is empty"
        counter = 0
        itr = self.head
        while itr:
            if counter == (self.getLength()-1) -1:
                itr.next = None
            counter += 1
            itr = itr.next

    def removeStart(self):
        if self.head == None: return "List is empty"
        self.head = self.head.next

    def showList(self):
        if self.head == None: return "List is empty"
        llist = ""
        itr = self.head
        while itr:
            llist += str(itr.data) + " "
            itr = itr.next
        return llist

if __name__=='__main__':
    ll = LinkedList()

    lis = [1,2,3,4,5]
    ll.insertList(lis)
    ll.removeEnd()
    print(ll.showList())