import globals
#import TwoWayNode, CharNode, PlayerNode, AllyNode, FoeNode
#import LinkedList, CircularLinkedList
#from AllyNode import AllyNode as aNode
from classes import *

if __name__ == '__main__':
    print("Initializing Globals...")
    globals.initialize()
    print("Initializing testAlly...")
    testAlly = AllyNode('friendDummy', 1, 50)
    testFoe = FoeNode('foeDummy', 2, 50)
    print(testAlly.getName(), testAlly.getPriority(), testAlly.getMaxHP())
    testAlly.performTurn()
    print(testFoe.getName(), testFoe.getPriority(), testFoe.getMaxHP())
    testFoe.performTurn()
