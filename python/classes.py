import globals

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

    def clone(self):
        return self

class CharNode(TwoWayNode):
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(head, tail)
        self.IS_AI = False
        self.IS_ALLY = False
        self.NAME = charName
        self.priority = priority
        self.maxHP = maxHP
        self.battleHP = maxHP
        self.abilityList = []

    def getName(self):
        return self.NAME

    def getPriority(self):
        return self.priority

    def getAI(self):
        return self.IS_AI
    
    def getAlly(self):
        return self.IS_ALLY

    def setMaxHP(self, newMax):
        self.maxHP = newMax
        
    def getMaxHP(self):
        return self.maxHP
    
    def setBattleHP(self, newHP):
        return self.newHP

    def getBattleHP(self):
        return self.battleHP
    
    def damage(self, damInt):
        self.battleHP -= damInt
    
    def setAbilityList(self, newList):
        self.abilityList = newList
    
    def getAbilityList(self):
        return self.abilityList()

    def addAbility(self, newAbility):
        self.abilityList.append(newAbility)
    
    def removeAbility(self, targetAbility):
        self.abilityList.remove(targetAbility)
    
    def performTurn(self):
        pass

class PlayerNode(CharNode):
    def __init(self, priority, maxHP, name, head = None, tail = None):
        super().__init__(priority, maxHP, name, head, tail)
        self.IS_AI = False
        self.IS_ALLY = True

class AllyNode(CharNode):
    def __init__(self, charName, priority, maxHP,  head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
        self.IS_AI = True
        self.IS_ALLY = True
        self.instructions = "pass"
        self.loadInstructions()

    def loadInstructions(self):
        for item in globals.charRoot.findall('./friends'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def getInstructions(self):
        return self.instructions

    def performTurn(self):
        eval(self.instructions)

class FoeNode(CharNode):
    def __init__(self, priority, maxHP, name, head = None, tail = None):
        super().__init__(priority, maxHP, name, head, tail)
        self.IS_AI = True
        self.IS_ALLY = False
        self.instructions = "pass"
        self.loadInstructions()

    def loadInstructions(self):
        for item in globals.charRoot.findall('./foes'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def getInstructions(self):
        return self.instructions

    def performTurn(self):
        eval(self.instructions)

class LinkedList():
    def __init__(self, length = 0, items = []):
        self.length = length
        self.items = items
    
    def insert(self, item, index =- 1):
        #TODO: Insert a TwoWayNode
        pass

    def pop(self, index = -1):
        #TODO: Pop the final node
        pass

    def getLength(self):
        return(self.length)

class CircularLinkedList(LinkedList):
    def __init__(self, length = 0, items = []):
        super().__init__()

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