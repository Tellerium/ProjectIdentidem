import xml.etree.ElementTree as ET
import math, time, classes

def init():
    global xTree
    global xRoot
    global frame
    global seed
    global crossTree
    global maxDepth
    global crossIndex
    global depthSum

    xTree = ET.parse('./xml/content.xml')
    xRoot = xTree.getroot()
    frame = 'title'
    seed = 0
    crossIndex = 0
    maxDepth = 5
    depthSum = tri_sum(maxDepth)
    crossTree = bloom()

def save():
    saveDict = {
        'seed':str(seed),
        'index':str(crossTree.index),
        'maxDepth':str(maxDepth),
        'depthSum':str(depthSum)
    }
    save = ET.parse('./xml/save_template.xml')
    saveRoot = save.getroot()
    for item in saveRoot:
        if item.tag in saveDict:
            item.text = saveDict.get(item.tag)
    save.write('./xml/save.xml')

def load():
    global seed
    global maxDepth
    global depthSum
    global crossIndex
    global crossTree
    load = ET.parse('./xml/save.xml')
    loadRoot = load.getroot()
    
    seed = int(loadRoot.find('./seed').text)
    index = int(loadRoot.find('./index').text)
    maxDepth = int(loadRoot.find('./maxDepth').text)
    depthSum = int(loadRoot.find('./depthSum').text)

    crossIndex = 0
    baseTree = bloom()
    crossTree = baseTree.find_index(index)
    




def new_seed():
    newSeed = (int(math.sqrt((math.pi * math.cos(time.time()) * time.time()) ** 2) // 2))
    return newSeed

def bloom():
    crossIndex = 0
    bloom = classes.TreeNode(0, maxDepth)
    return(bloom)

def get_rand(pos):
    posIn = pos
    refSeed = str(seed)
    if posIn >= len(refSeed) - 1:
        posIn = len(refSeed) - 1
    rand = int(refSeed[posIn])
    return(rand)


def tri_sum(triNum):
    triSum = 0
    for n in range(0, triNum + 1):
        triSum += 2 ** n
    return triSum

def parse_content(content):
    encounterDict = {
            '0':'',
            '1':'',
            '2':'',
            '3':'',
            '4':'',
            '5':'',
            '6':'',
            '7':'',
            '8':'',
            '9':'',
        }
    allyDict = {
            '0':'',
            '1':'',
            '2':'',
            '3':'',
            '4':'',
            '5':'',
            '6':'',
            '7':'',
            '8':'',
            '9':'',
        }
    itemDict = {
            '0':'',
            '1':'',
            '2':'',
            '3':'',
            '4':'',
            '5':'',
            '6':'',
            '7':'',
            '8':'',
            '9':'',
        }