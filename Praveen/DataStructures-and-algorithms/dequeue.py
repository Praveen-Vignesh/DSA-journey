class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = self.prev = None

class DeQueue:
    def __init__(self, front, rear):
        self.front = self.rear = None
    
    def enQueueFront(self, val): #insert
        newNode = Node(val)

        if not self.front:
            self.front = newNode
            self.rear = newNode
            return
        
        self.front.nxt = newNode
        self.front = self.front.nxt
        return

    def enQueueBack(self, val):
        newNode = Node(val)

        if not self.rear:
            self.rear = newNode
            self.front = newNode
            return
        
        self.rear.prev = newNode
        self.rear = self.rear.prev; return

    def deQueueFront(self):
        if not self.front: return

        temp = self.front
        self.front = self.front.nxt
        del temp

        return self.front
    
    def deQueueBack(self):
        if not self.rear: return

        temp = self.rear
        self.rear  = self.rear.prev
        del temp    