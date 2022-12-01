import xml.etree.ElementTree as ET

def init():
    global charTree
    charTree = ET.parse('./xml/characters.xml')
    global charRoot
    charRoot = charTree.getroot()
