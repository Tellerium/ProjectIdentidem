import xml.etree.ElementTree as ET
import math, time

def init():
    global charTree
    global charRoot
    global seed
    global frame
    
    charTree = ET.parse('./xml/characters.xml')
    charRoot = charTree.getroot()
    seed = 0
    frame = 'title'

def newSeed():
    return (int(math.sqrt((math.pi * math.cos(time.time()) * time.time()) ** 2) // 2))