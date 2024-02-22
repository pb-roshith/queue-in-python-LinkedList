class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        return self.front is None
        
    def enqueue(self, data):
        new = Node(data)
        if self.isEmpty():
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
    
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        d = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return d
    
    def traverse(self):
        curr = self.front
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.isEmpty())
queue.traverse()
print(queue.dequeue())
print(queue.dequeue())
