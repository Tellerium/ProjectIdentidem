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

class TreeNode(TwoWayNode):
    def __init__(self, depth, maxDepth, head = None, tail = None):
        super().__init__(head, tail)
        self.index = globals.crossIndex
        self.depth = depth
        self.maxDepth = maxDepth
        self.content = self.get_content()
        globals.crossIndex += 1
        if self.depth < maxDepth:
            self.tail = [TreeNode(depth + 1, maxDepth, self), TreeNode(depth + 1, maxDepth, self)]
        
    def find_index(self, index):
        print("Found index", self.index)
        if self.index == index:
            return self
        elif self.tail is not None:
            leftBranch = self.tail[0].find_index(index)
            if leftBranch is not None and leftBranch.index == index:#TODO: Check this for redundancy
                return leftBranch
            rightBranch = self.tail[1].find_index(index)
            return rightBranch
    
    def get_content(self):
        encounterDict = {
            '0':'enc0',
            '1':'enc1',
            '2':'enc2',
            '3':'enc3',
            '4':'enc4',
            '5':'enc5',
            '6':'enc6',
            '7':'enc7',
            '8':'enc8',
            '9':'enc9',
        }
        allyDict = {
            '0':'ally0',
            '1':'ally1',
            '2':'ally2',
            '3':'ally3',
            '4':'ally4',
            '5':'ally5',
            '6':'ally6',
            '7':'ally7',
            '8':'ally8',
            '9':'ally9',
        }
        itemDict = {
            '0':'item0',
            '1':'item1',
            '2':'item2',
            '3':'item3',
            '4':'item4',
            '5':'item5',
            '6':'item6',
            '7':'item7',
            '8':'item8',
            '9':'item9',
        }

        type = globals.get_rand(int(str(self.index)[0])) % 3
        option = (globals.get_rand(int(str(self.index)[1])) % 10 if self.index >= 10 else globals.get_rand(int(str(self.index))) % 10)
        match type:
            case 2:
                type = "Encounter"
                option = encounterDict.get(str(option))
            case 1:
                type = "Ally"
                option = allyDict.get(str(option))
            case 0:
                type = "Item"
                option = itemDict.get(str(option))
        return(type, option)

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
        return newHP

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
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
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
        for item in globals.xRoot.findall('./characters/friends'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def get_instructions(self):
        return self.instructions

    def turn(self):
        eval(self.instructions)

class FoeNode(CharNode):
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
        self.IS_AI = True
        self.IS_ALLY = False
        self.instructions = "pass"
        self.loadInstructions()

    def load_instructions(self):
        self.instructions = "No Instructions"
        # for item in globals.xRoot.findall('./characters/foes'):
        #     for child in item:
        #         if child.tag == self.NAME:
        #             #self.instructions = child.text
        #             self.instructions = "none"

    def get_instructions(self):
        return self.instructions

    def turn(self):
        eval(self.instructions)

class LinkedList():
    def __init__(self, items = []):
        self.items = []
        for item in items:
            print("In,", item)
            if len(self.items) != 0:
                item.head = self.items[-1]
            self.items.append(item)
            if len(self.items) >= 2:
                self.items[-2].tail = self.items[-1]
            print("Attached,", self.items)
        print("Items,", self.items)
        self.focus = items[0]
    
    def insert(self, item):
        item.head = self.items[-1]
        item.tail = None
        self.items.append(item)

    def pop(self, index = -1):
        self.items.pop(-1)
        self.items[-1].tail = None

    def get_length(self):
        return(len(self.items))

    def next(self):
        self.focus = self.focus.tail

class CircularLinkedList(LinkedList):
    def __init__(self, items = []):
        super().__init__(items)
        self.ouroboros_helper()

    def insert(self, item):
        super().insert()
        self.ouroboros_helper()

    def pop(self, index = -1):
        super().pop()
        self.ouroboros_helper()

    def ouroboros_helper(self):
        self.items[-1].tail = self.items[0]
