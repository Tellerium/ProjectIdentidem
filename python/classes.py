import globals

class TwoWayNode():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def set_head(self, newHead):
        self.head = newHead

    def get_head(self):
        return self.head

    def set_tail(self, newTail):
        self.tail = newTail

    def get_tail(self):
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

    def get_name(self):
        return self.NAME

    def get_priority(self):
        return self.priority

    def get_AI(self):
        return self.IS_AI
    
    def get_Ally(self):
        return self.IS_ALLY

    def set_maxHP(self, newMax):
        self.maxHP = newMax
        
    def get_maxHP(self):
        return self.maxHP
    
    def set_battleHP(self, newHP):
        return self.newHP

    def get_battleHP(self):
        return self.battleHP
    
    def damage(self, damInt):
        self.battleHP -= damInt
    
    def set_ability_list(self, newList):
        self.abilityList = newList
    
    def get_ability_list(self):
        return self.abilityList()

    def add_ability(self, newAbility):
        self.abilityList.append(newAbility)
    
    def remove_ability(self, targetAbility):
        self.abilityList.remove(targetAbility)
    
    def turn(self):
        pass

class PlayerNode(CharNode):
    def __init__(self, priority, maxHP, name, head = None, tail = None):
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

    def load_instructions(self):
        for item in globals.charRoot.findall('./friends'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def get_instructions(self):
        return self.instructions

    def turn(self):
        eval(self.instructions)

class FoeNode(CharNode):
    def __init__(self, priority, maxHP, name, head = None, tail = None):
        super().__init__(priority, maxHP, name, head, tail)
        self.IS_AI = True
        self.IS_ALLY = False
        self.instructions = "pass"
        self.loadInstructions()

    def load_instructions(self):
        for item in globals.charRoot.findall('./foes'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def get_instructions(self):
        return self.instructions

    def turn(self):
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

    def get_length(self):
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
    
    def get_length(self):
        return(self.length)

    def ouroboros_helper(self):
        #TODO: Feed the snake its tail
        pass