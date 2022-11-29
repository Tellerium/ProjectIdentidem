class TwoWayNode():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def setHead(self, newHead):
        self.head = newHead

    def getHead(self):
        return self.head

    def setTail(self, newTail):
        self.tail = newTail

    def getTail(self):
        return self.tail