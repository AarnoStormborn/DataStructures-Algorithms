from dataclasses import dataclass

@dataclass
class QNode:
    data: int = None
    next: int = None

@dataclass
class Queue:
    head: int = None

    def enqueue(self, data):
        if self.head is None:
            qnode = QNode(data, None)
            self.head = qnode
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = QNode(data, None)

    def dequeue(self):
        if self.head is None: return None
        item = self.head.data
        self.head = self.head.next
        return item 

    def isEmpty(self):
        if self.head == None: return True
        else: return False

@dataclass
class Node:
    data : int = None
    left : int = None
    right: int = None

@dataclass
class BinaryTree:
    root: int = None

    def display_tree(self):
        if self.root == None: return
    
        q = Queue()
        tree = self.root
        q.enqueue(tree)
        while not q.isEmpty():
            tree = q.dequeue()
            print(tree.data, end= " ")
            if tree.left is not None:
                q.enqueue(tree.left)
            if tree.right is not None:
                q.enqueue(tree.right)
            
    def height(self):
        return self._height_(self.root)

    def _height_(self, tree):
        if self.root is None:
            return 0

        tree = self.root
        lheight = self._height_(tree.left) #height of left subtree
        rheight = self._height_(tree.right) #height of right subtree

        if lheight>rheight: return lheight + 1
        else: return rheight + 1 

    def add_child(self, data):
        if self.root is None:
            node = Node(data, None, None)
            self.root = node
            return

        q = Queue()
        tree = self.root
        q.enqueue(tree)
        while not q.isEmpty():
            if tree.left == None:
                tree.left = Node(data, None, None)
                break
            else:
                q.enqueue(tree.left)
            if tree.right == None:
                tree.right = Node(data, None, None)
                break
            else:
                q.enqueue(tree.right)
            tree = q.dequeue()


# Driver code
if __name__=='__main__':
    bt = BinaryTree()

    inp = [31, 2, 44, 27, 19]
    for i in inp:
        bt.add_child(i)

    bt.display_tree()