import LinkedList

class CircularLinkedList(LinkedList):
    def __init__(self, length = 0, items = []):
        self.length = length
        self.items = items
    
    def insert(self, item, index =- 1):
        #TODO: Overwrite to include Ouroboros
        pass

    def pop(self, index = -1):
        #TODO: Same as insert
        pass
    
    def getLength(self):
        return(self.length)

    def ouroborosHelper(self):
        #TODO: Feed the snake its tail
        pass