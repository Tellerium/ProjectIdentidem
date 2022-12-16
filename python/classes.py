"""
classes.py
Created: Nov. 2022
Updated: 15 Dec. 2022
Author: Trystan X. Hearing

This module serves as a place to store the classes that are meant
to be instantiated in the package. It also stores abstract parents.

Getters & Setters are largely unused because they're not instinct.

#==FUNCTIONS==#
| TwoWayNode (`TWN`) is the base for most other classes.
| TreeNode is a bifurcated TWN for spawning binary trees.
| CharNode (`CN`) is the base skeleton for all character types.
| PlayerNode is a specialized CN meant to be controlled directly.
| AllyNode is a specialized CN meant to be friendly.
| FoeNode is a specialized CN meant to be oppositional.
| LinkedList (`LL`) holds doubly-linked TWNs in a list.
| CircularLinkedList is an LL whose head and tail are connected.
"""

import globals

class TwoWayNode():
    """`TWN` is the base for most other classes.
    
    The TWN is composed of a head and a tail.
    It can clone itself if need be.
    Its generic nature makes it ideal for an ancestor class.
    """
    
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
    """A bifurcated TWN for spawning binary trees.
    
    Each node possesses a head and bifurcated tail.
    The origin node is headless, but all of its descendants take
    their nearest ancestor as a head.

    Nodes are created recursively until the given maximum depth is
    achieved. Additionally, each node knows its depth and is given
    a unique index and pseudo-randomized content.
    #===========#
    | Functions |
    #===========#
    | find_index() returns the node with the given index.
    | get_content() returns the content type and option.
    #===========#
    | Variables |
    #===========#
    | index is a UUID associated with the node. Unique per tree.
    | depth is the depth level in which the node resides.
    | maxDepth is the depth at which recursion ceases.
    | content stores what the type of content that is in the cell
    alongside what option within that type should be used. This is
    largely used to be parsed by outside forces.
    """
    
    def __init__(self, depth, maxDepth, head = None, tail = None):
        super().__init__(head, tail) # Commune with the ancestors
        self.index = globals.crossIndex # Imprint UUID
        globals.crossIndex += 1 # Increase UUID for next node
        self.depth = depth # Imprint the current depth level
        self.maxDepth = maxDepth # Pass it along
        self.content = self.get_content() # See Docstring
        # Recurse the bifurcated tail if there is more depth
        if self.depth < maxDepth:
            self.tail = [TreeNode(depth + 1, maxDepth, self),
                        TreeNode(depth + 1, maxDepth, self)]
        
    def find_index(self, index):
        """Returns the node with the given index.
        
        Use recursion to first search the left nodes to the maximum
        depth and then searches the right nodes as it continues up.
        """
        
        # Return the node if it has the target index
        if self.index == index:
            return self
        # Recurisvely check the tail nodes
        elif self.tail is not None:
            leftBranch = self.tail[0].find_index(index) # Search left
            # Return the left branch if it contains the node we want
            if leftBranch is not None and leftBranch.index == index:
                return leftBranch
            # If the left hasn't the index, the right will in time
            rightBranch = self.tail[1].find_index(index)
            return rightBranch
    
    def get_content(self):
        """Returns the content type and option.
        
        First, the type of content is decided through the global
        get_rand() then the relevant dictionary is rolled upon to
        determine which option is given. Both type and content are
        returned in a list.

        The higher case values are more likely.
        """

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

        # Roll the type and option values
        type = globals.get_rand(int(str(self.index)[0])) % 3
        option = (globals.get_rand(int(str(self.index)[1])) % 10
            if self.index >= 10
            else globals.get_rand(int(str(self.index))) % 10)
        # Determine the correct dictionary, then get the option
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
    """(`CN`) is the base skeleton for all character types.
    

    #===========#
    | Functions |
    #===========#
    | damage() subtracts the given value from battleHP.
    | turn() exists as a failsafe for descendants. Unused.
    #===========#
    | Variables |
    #===========#
    | IS_AI determines wether controlled directly or remotely.
    | IS_ALLY determines whether friend or foe.
    | NAME is the UUID for the character.
    | priority would have been used to sort order of turns. Unused.
    | maxHP provides a baseline and cap for battleHP.
    | battleHP is used during to determine death.
    | abilityList would have determined actions available. Unused.
    """
    
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(head, tail)
        self.IS_AI = False # Safety. Gives direct control
        self.IS_ALLY = False # Safety. Might need to purge foe
        self.NAME = charName # Esatblish UUID
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
        """Subtract the damInt from battleHP."""
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
        """Safety feature for descendants. Unused."""
        pass

class PlayerNode(CharNode):
    """Specialized CN meant to be controlled directly."""
    
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
        self.IS_AI = False # Player controlled
        self.IS_ALLY = True # Not my own enemy

class AllyNode(CharNode):
    """Specialized CN meant to be friendly.
    
    #==FUNCTIONS==#
    | load_instructions() loads in the AI from an XML file.
    | turn() performs the AI when called. Unused
    #==Variables==#
    | instructions store an eval statement that performs the AI.
    """
    
    def __init__(self, charName, priority, maxHP,  head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
        self.IS_AI = True # Not player controlled
        self.IS_ALLY = True # Frenly :-)
        self.instructions = "pass" # Safety. Skips when no AI
        self.loadInstructions() # Assign AI

    def load_instructions(self):
        """Loads in the AI from an XML file."""
        #Parse XML and grab instructions
        for item in globals.xRoot.findall('./characters/friends'):
            for child in item:
                if child.tag == self.NAME:
                    self.instructions = child.text

    def get_instructions(self):
        return self.instructions

    def turn(self):
        """Perform recalled instructions. Unused."""
        eval(self.instructions)

class FoeNode(CharNode):
    """Specialized CN meant to be oppositional.
    
    #==FUNCTIONS==#
    | load_instructions() loads in the AI from an XML file. Unused.
    | turn() performs the AI when called. Unused
    #==Variables==#
    | instructions store an eval statement that performs the AI.
    """
    def __init__(self, charName, priority, maxHP, head = None, tail = None):
        super().__init__(charName, priority, maxHP, head, tail)
        self.IS_AI = True # Non player controlled
        self.IS_ALLY = False # Non frenly :-(
        self.instructions = "pass" # Safety.
        self.loadInstructions() # Assign AI

    def load_instructions(self):
        """Loads in the AI from an XML file. Unused"""
        self.instructions = "pass"
        # for item in globals.xRoot.findall('./characters/foes'):
        #     for child in item:
        #         if child.tag == self.NAME:
        #             #self.instructions = child.text
        #             self.instructions = "none"

    def get_instructions(self):
        return self.instructions

    def turn(self):
        """Perform recalled instructions. Unused."""
        eval(self.instructions)

class LinkedList():
    """(`LL`) holds doubly-linked TWNs in a list.
    
    Each LL contains a list of TWNs which are double-connected
    amongst each other, once by the head and once by the tail.
    
    Items can be inserted to the end and popped from the end.

    #===========#
    | Functions |
    #===========#
    | insert() attaches the item's head and places it in the list.
    | pop() removes the item and cut's the remaining tail.
    #===========#
    | Variables |
    #===========#
    | items is the list of the connected nodes
    | focus is the currently focused node. Useful to externals.
    """

    def __init__(self, items = []):
        self.items = [] # Initialize empty list
        # Initialize the items
        for item in items:
            # Watch the head
            if len(self.items) != 0:
                item.head = self.items[-1]
            self.items.append(item)
            # Set the tail on the penultimate TWN
            if len(self.items) >= 2:
                self.items[-2].tail = self.items[-1]
        self.focus = items[0] # Initialize focus
    
    def insert(self, item):
        """Attach item's head and place it in the list"""
        item.head = self.items[-1] # Attach head
        item.tail = None # Safety. Clean tail
        self.items.append(item) # Place in list
        self.items.tail[-2] = self.items[-1] # Link tail

    def pop(self, index = -1):
        """Removes the item and cut's the remaining tail"""
        self.items.pop(-1) # Throw him to the dogs
        self.items[-1].tail = None # Break the weak link

    def get_length(self):
        return(len(self.items))

class CircularLinkedList(LinkedList):
    """LL whose head and tail are connected.
    
    An LL with a first element whose head is the last element
    and a last element whose tail is the first element.

    #==FUNCTIONS==#
    | ouroboros_helper() stitches the circle shut.
    | next() moves the focus to the next element.
    | prev() moes the focus to the previous element.
    """
    
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
        """Attaches the head and tail. Think of the serpent."""
        self.items[0].head = self.items[-1]
        self.items[-1].tail = self.items[0]
        
    def next(self):
        self.focus = self.focus.tail

    def prev(self):
        self.focus = self.focus.head
