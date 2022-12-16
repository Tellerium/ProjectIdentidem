"""
globals.py
Created: Nov. 2022
Updated: 15 Dec. 2022
Author: Trystan X. Hearing

This module serves as a place to store variables and functions
that are meant to be accessed easily by all files in the package.

#==FUNCTIONS==#
| init() should be called to initialize all the variables. Note that
this is not the same as `__init__`.
| save() stores the global variables based off of an xml template.
| load() loads the global variables from an xml file.
| new_seed() generates a pseudo-random seed based off the time.
| bloom() generates a balanced binary tree based off of the seed.
| get_rand() grabs a pseudo-random number from the seed.
| tri_sum() calculates the triangular sum of 2^n.
"""

import xml.etree.ElementTree as ET
import math, time, classes

def init():
    """Initializes the `superglobal` variables.
    
    The program depends on this being called before any frame.
    Additionally, the program cannot parse without it.
    This is not to be confused with a classical `__init__`.
    """
    # Establish the global variables
    global xTree # Used with xRoot to parse XML data
    global xRoot
    global frame # Used to track what `frame` to draw
    global seed # Used to pick pseudo-random values
    global crossTree # A binary tree. Contains two-way tree nodes
    global maxDepth # The deepest layer that should be generated
    global crossIndex # Gives a unique index to each tree node
    global depthSum # Used to ensure safety when traversing trees
    global party # Largely defunct. Tracks a persistent party

    # Setup the XML parsing variables
    xTree = ET.parse('./xml/content.xml')
    xRoot = xTree.getroot()
    # Draw the title frame on boot
    frame = 'title'
    # Prepare for the tree to be born
    seed = 0
    crossIndex = 0
    maxDepth = 5
    depthSum = tri_sum(maxDepth)
    # Birth the tree
    crossTree = bloom()
    # Set the starting party
    party = ["Hannah"]

def save():
    """Stores the global variables based off of an xml template.
    
    | saveDict exists to keep the code orderly when parsing.
    | save is the file where the save template is stored.
    | saveRoot is used for XML parsing.
    """

    saveDict = {
        'seed':str(seed),
        'index':str(crossTree.index),
        'maxDepth':str(maxDepth),
        'depthSum':str(depthSum)
    }
    # Setup the XML parsing variables
    save = ET.parse('./xml/save_template.xml')
    saveRoot = save.getroot()
    # Assemble the template and retrieve the values
    for item in saveRoot:
        if item.tag in saveDict:
            item.text = saveDict.get(item.tag)
    # Save the values (not in the template file)
    save.write('./xml/save.xml')

def load():
    """Loads the global variables from an xml file.

    This function loads the global variables stored in `save.xml`
    to the running program. Afterward, it generates a new tree.

    | load is the file where the save is stored.
    | loadRoot is used for xml parsing.
    """
    
    # Head-off reference issues (It's my turn on the variables!)
    global seed
    global maxDepth
    global depthSum
    global crossIndex
    global crossTree
    # Setup the XML parsing variables
    load = ET.parse('./xml/save.xml')
    loadRoot = load.getroot()
    # Load the non-volatile global variables
    seed = int(loadRoot.find('./seed').text)
    index = int(loadRoot.find('./index').text)
    maxDepth = int(loadRoot.find('./maxDepth').text)
    depthSum = int(loadRoot.find('./depthSum').text)
    # From the lost hand, birth the forgotten petals.
    crossIndex = 0
    baseTree = bloom()
    crossTree = baseTree.find_index(index)

def new_seed():
    """Generates a pseudo-random seed based off the time.
    
    The seed is drawn from the system clock and then placed through
    mathematical transformations to prevent seeds created in close
    timing from being too similar. Finally the seed undergoes
    meiosis to achieve further lengths.

    The transformation constants are largely arbitrary.
    """

    seedTime = time.time() # Pull time
    # Transform the seed
    newSeed = str(int(math.sqrt(
        (math.pi * math.cos(seedTime) * seedTime) ** 2)
        // 2)) # Cut off any decimal values
    # Meiosis occurs
    newSeed = int(newSeed + newSeed[0:4] + newSeed[-4:] + newSeed[4:6])
    return newSeed

def bloom():
    """Generates a balanced binary tree based off of the seed.
    
    The tree is generated using nodes with a single head and a
    bifurcated (double-ended) tail. Each node knows its depth.
    Nodes will stop generating at the maximum depth.

    The origin node will recursively create tail nodes.
    Head over to `classes.py` for more details.
    
    As it is built, each node is given a unique index value.
    This value is reused when loading the correct placement.
    """

    crossIndex = 0 # Reset the UUID stamping machine
    bloom = classes.TreeNode(0, maxDepth) # Generate origin node
    return(bloom)

def get_rand(pos):
    """Grabs a pseudo-random number from the seed.
    
    Pulls a number from the seed, treating the passed-in value as
    the index from which to pull the number. If, somehow, the
    passed-in value is out-of-bounds, it will instead pull from
    the final number in the seed.

    | pos is the index of the seed to be extracted from.
    """

    refSeed = str(seed) # Store a String of the current seed
    # Safety check (At a certain depth, this will be the same)
    if pos >= len(refSeed) - 1:
        pos = -1
    rand = int(refSeed[pos]) # Parse the seed
    return(rand)

def tri_sum(triNum):
    """Calculates the triangular sum of 2^n.
    
    For reference this is the summation of (2^0 + 2^1 + ... 2^n).
    """

    triSum = 0 # Initialize the sum
    # Calculate the sum through iteration
    for n in range(0, triNum + 1):
        triSum += 2 ** n
    return triSum