import xml.etree.ElementTree as ET
import math, time

def init():
    global charTree
    global charRoot
    global frame
    global seed
    global maxDepth
    global crossIndex
    global depthSum

    charTree = ET.parse('./xml/characters.xml')
    charRoot = charTree.getroot()
    frame = 'title'
    seed = 0
    crossIndex = 0
    maxDepth = 5
    depthSum = tri_sum(maxDepth)

def new_seed():
    return (int(math.sqrt((math.pi * math.cos(time.time()) * time.time()) ** 2) // 2))

def tri_sum(triNum):
    triSum = 0
    for n in range(0, triNum + 1):
        triSum += 2 ** n
    return triSum
