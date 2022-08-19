from dataclasses import dataclass
import numpy as np 
from time import time

@dataclass
class SQnode:
    data: int = None
    next: int = None

@dataclass
class Queue:
    head: int = None

    def enqueue(self, data):
        if self.head == None:
            node = SQnode(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = SQnode(data, None)

    def dequeue(self):
        if self.head == None: return
        item = self.head.data
        self.head = self.head.next
        return item

    def isEmpty(self):
        if self.head == None: return True
        return False

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
        node = SQnode(data, self.head)
        self.head = node

    def pop(self):
        if self.head == None: return
        item = self.head.data
        self.head = self.head.next
        return item
        
    def isEmpty(self):
        if self.head == None: return True
        return False

@dataclass
class Node:
    data: int = None
    left: int = None
    right: int = None

@dataclass
class BinarySearchTree:
    root: int = None 
    
    def level_order_traversal(self):
        """Breadth First Traversal of Binary Search Tree"""
        if self.root == None:return

        q = Queue()
        tree = self.root
        q.enqueue(tree) #enqueue the root (level 0) of the tree
        while not q.isEmpty():
            tree = q.dequeue() # pop the item enqueued then print
            print(tree.data, end=" ")
            if tree.left != None: q.enqueue(tree.left)
            if tree.right != None: q.enqueue(tree.right)

    def in_order_traversal(self):
        """Depth First Traversal - prints the BST in sorted order"""

        if self.root == None: return
        
        s = Stack()
        tree = self.root
        while tree!=None or not s.isEmpty(): 
            if tree != None: # travels to the farthest node on left
                s.push(tree)
                tree = tree.left
            else:               #when left node is reached, pop item and print and then traverse right tree
                tree = s.pop() 
                print(tree.data, end=" ")
                tree = tree.right

    def pre_order_traversal(self):
        """Depth First Traversal- Root=> Left subtree=> Right subtree"""

        if self.root == None: return

        s = Stack()
        tree = self.root
        while tree!=None or not s.isEmpty(): 
            if tree != None: # travels to the farthest node on left
                print(tree.data, end=" ")
                s.push(tree)
                tree = tree.left
            else:               #when left node is reached, pop item and print and then traverse right tree
                tree = s.pop() 
                tree = tree.right

    def insert(self, data):
        if self.root == None:
            self.root = Node(data, None, None)
            return
        tree = self.root
        while tree: # while the leaf node is not found
            if data < tree.data:
                if tree.left == None: #check for leaf node
                    tree.left = Node(data, None, None)
                    return
                tree = tree.left # further into left tree until we find leaf node
            elif data > tree.data:
                if tree.right == None: #check for leaf node
                    tree.right = Node(data, None, None)
                    return
                tree = tree.right # further into right tree until we find leaf node
            # else: pass
        
    def maximum(self):
        if self.root == None: return
        tree = self.root
        while tree.right:
            tree = tree.right
        return tree.data

    def minimum(self):
        if self.root == None: return
        tree = self.root
        while tree.left:
            tree = tree.left
        return tree.data

    def search(self, element): ## TODO Fix this function
        if self.root == None: return
        flag = 0
        tree = self.root
        while tree: # while the leaf node is not found
            if element == tree.data:return True #check data at root
            
            elif element < tree.data:   #checking left subtree
                if element == tree.data: flag = 1
                tree = tree.left        # further into left tree until we find leaf node
            
            elif element > tree.data:
                if element == tree.data: flag = 1
                tree = tree.right       # further into right tree until we find leaf node  
            
        return True if flag == 1 else False

    
    def recur_search(self, key):
        tree = self.root
        return self._recur_search_(tree, key)
    
    def _recur_search_(self, root, key):
        if root == None: return False
        if root.data == key: return True
        if self._recur_search_(root.left, key): return True
        if self._recur_search_(root.right, key): return True
        else: return False


    def delete_element(self, element):
        pass


# Driver code
if __name__=='__main__':

    bst = BinarySearchTree()

    n=int(input("\nEnter size: "))
    inp = np.random.rand(n)

    start = time()
    for val in inp:
        bst.insert(val)
    print(f'Inserted {n} values\nTime taken: {time()-start}')

