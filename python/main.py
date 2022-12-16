"""
main.py
Created: Nov. 2022
Updated: 15 Dec. 2022
Author: Trystan X. Hearing

#==DEPENDENCIES==#
| Python 3.10
| Pygame

This module is the main module for playing the game.
It also contains the pygame code to display everything.

This is largely built around the frame system. The least important
frame is run first each loop, with the frame to be persisted
stored as a global variable. Each frame kills itself when not
focused on.

Not all the functions and variables are listed for everything in
this package. Only those that I feel are important or may need
further explanation than easily provided.

#============#
|  CONTROLS  |
#============#
`Z` - Return to the previous frame
`ESC` - Kill the game with autosave
`F` - Toggle Fullscreen
`UP/DOWN` (On Title) - Navigate Menu
`UP/LEFT/RIGHT` (Crossroads) - Navigate Tree

#==FUNCTIONS==#
| get_font() creates a pygame font object to be displayed.
| game() plays the game, maintaining the necessary loop.
| title() is the title screen.
| options() was repurposed into a test battle.
| crossroads() is a navigable pseudo-random tree.
| new_game() creates a new tree and goes to the crossroads.
| load_game() loads the autosave and goes to the crossroads.

#==REGRETS==#
| I would refactor much of the pygame code. This largely concerns
the common navigation functions in the primary frames. I would also
have created a text constructor that created the text, rect, and
positioned the rect all at once.
| I wasn't able to add functionality to the crossroads.
| I wasn't able to implement battles in general.
| Not really a game.
"""

import globals, pygame, sys
from classes import *

# Settings for initalizing pygame
pygame.init()
SCREEN = (1280, 720) # Default screen size
WINDOW = pygame.display.set_mode(SCREEN, pygame.SCALED) # Scale Screen
ICON = pygame.image.load("./assets/images/test.ico")
pygame.display.set_caption("Project Identidem")
pygame.display.set_icon(ICON)

def get_font(size, fontKey):
    """Creates a pygame font object to be displayed."""
    fontDict = {
        'title':'StarConstellation-87zn',
        'text':'Quicksand-Regular'
    }
    return pygame.font.Font(str("./assets/fonts/" +
            fontDict[fontKey] + ".ttf"), size)

def game():
    globals.init()
    while True:
        options()
        crossroads()
        title()

def title():
    """The title screen.
    
    From the title screen, a tree may be created or loaded.
    There is a proof of concept of turn-based action in options.
    Additionally, the game may be quit from here.

    #==VARIABLES==#
    | textIndex is used to track the selected option
    | indexChanged is used to determine if an option should
    be highlighted.
    """
    
    # Initialize Window
    WINDOW.fill("white")
    pygame.display.set_caption("Project_Identidem")
    
    # Create Title Text
    # Set Text
    titleText = get_font(64, 'title').render("Identidem",
                    True, 'Purple')
    # Get Rectangles
    titleRect = titleText.get_rect()
    # Position Rectangles
    titleRect.move_ip(480, 72)
    # Draw Rectangles
    WINDOW.blit(titleText, titleRect)

    # Initialize Buttons
    # Text Dictionaries
    textIndex = 0 # Initialize to `New Loop`
    indexChanged = False
    textDict = {
        '0':'New Loop',
        '1':'Resume Loop',
        '2':'Test Battle',
        '3':'Give Up'
    }
    textPos = {
        '0':(SCREEN[0]/2, 144),
        '1':(SCREEN[0]/2, 288),
        '2':(SCREEN[0]/2, 432),
        '3':(SCREEN[0]/2, 576)
    }
    
    # Create Choices Text
    # Set Text
    newText = get_font(32, 'text').render(textDict.get('0'),
                True, "Gray")
    loadText = get_font(32, 'text').render(textDict.get('1'),
                True, "Gray")
    settingsText = get_font(32, 'text').render(textDict.get('2'),
                True, "Gray")
    exitText = get_font(32, 'text').render(textDict.get('3'),
                True, "Gray")
    # Get Rectangles
    newRect = newText.get_rect()
    loadRect = loadText.get_rect()
    settingsRect = settingsText.get_rect()
    exitRect = exitText.get_rect()
    # Position Rectangles
    newRect.move_ip(textPos.get('0'))
    loadRect.move_ip(textPos.get('1'))
    settingsRect.move_ip(textPos.get('2'))
    exitRect.move_ip(textPos.get('3'))
    # Draw Rectangles
    WINDOW.blit(newText, newRect)
    WINDOW.blit(loadText, loadRect)
    WINDOW.blit(settingsText, settingsRect)
    WINDOW.blit(exitText, exitRect)

    # Create Selected Text
    selectedText = get_font(32, 'text').render(textDict.get(str(
                        textIndex)), True, "Blue")
    selectedRect = selectedText.get_rect()
    selectedRect.move_ip(textPos.get(str(textIndex)))
    WINDOW.blit(selectedText, selectedRect)

    # Perform Title Screen Processing
    while globals.frame == 'title':
        # Update Selected Text
        if indexChanged != -1:
            selectedText = get_font(32, 'text').render(textDict.get(
                            str(indexChanged)), True, "Gray")
            WINDOW.blit(selectedText, selectedRect)
            indexChanged = -1
            selectedText = get_font(32, 'text').render(textDict.get(
                            str(textIndex)), True,
                            "Blue" if textIndex != 3 else "Red")
            selectedRect = selectedText.get_rect()
            selectedRect.move_ip(textPos.get(str(textIndex)))
            WINDOW.blit(selectedText, selectedRect)
        # Handle Pygame events
        for event in pygame.event.get():
            # `X` Close button on window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle Input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_DOWN:
                    # Update Index
                    indexChanged = textIndex
                    textIndex = (textIndex + 1) % 4
                if event.key == pygame.K_UP:
                    # Update Index
                    indexChanged = textIndex
                    textIndex = (textIndex - 1) % 4
                if event.key == pygame.K_BACKSPACE:
                    if textIndex == 0:
                        new_Game()
                    elif textIndex == 1:
                        load_Game()
                    elif textIndex == 2:
                        globals.frame = 'options'
                    elif textIndex == 3:
                        pygame.quit()
                        sys.exit()
        pygame.display.update()

def new_Game():
    globals.seed = globals.new_seed() # Generate new seed
    globals.crossIndex = 0 # Reinitialize UUID Stamp
    globals.depthSum = globals.tri_sum(globals.maxDepth) # Safety
    globals.crossTree = globals.bloom() # Bloom new tree
    globals.frame = 'cross' # Move to the crossroads

def load_Game():
    globals.load() # Utilize the global load
    globals.frame = 'cross' # Move to the crossroads

def options():
    """Repurposed into a test battle.
    
    Showcases the CLL with the ability to damage the classes.
    The player may not exit the frame until either allyNum or
    foeNum reaches zero.
    """
    
    # Initialize Window
    pygame.display.set_caption('Options')
    WINDOW.fill("green")
    
    # Create the CLL
    ally = PlayerNode('Hannah', 1, 200) # Create Node 1
    foe = PlayerNode('Enemy',0,100) # Create Node 2
    circuitItems = [ally, foe] # List of Nodes for the CLL to stitch
    circuit = CircularLinkedList(circuitItems) # Create the CLL
    allyNum = circuit.focus.maxHP # Find the battleHP for Player
    # Find the battleHP for Foe
    circuit.next()
    foeNum = circuit.focus.maxHP
    circuit.next()

    # Create Ally and Foe Text
    # Set Text
    allyText = get_font(32, 'text').render(f'Allies: {allyNum}', True, "Gray")
    foeText = get_font(32, 'text').render(f'Foes: {foeNum}', True, "Gray")
    # Get Rectangles
    allyRect = allyText.get_rect()
    foeRect = foeText.get_rect()
    # Position Rectangles
    allyRect.move_ip(560, 120)
    foeRect.move_ip(560, 180)
    # Draw Rectangles
    WINDOW.blit(allyText, allyRect)
    WINDOW.blit(foeText, foeRect)

    # Battle Loop
    while (globals.frame == 'options' and allyNum > 0 and foeNum > 0):
        # Handle Pygame events
        for event in pygame.event.get():
            # `X` Close button on window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle Input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    globals.save()
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_x:
                    circuit.focus.damage(10)
                if event.key == pygame.K_c:
                    circuit.next()
                    circuit.focus.damage(10)
                    circuit.next()
                allyNum = circuit.focus.battleHP
                circuit.next()
                foeNum = circuit.focus.battleHP
                circuit.next()
        # Update Ally and Foe Text
        WINDOW.fill("green")
        # Set Text
        allyText = get_font(32, 'text').render(f'Allies: {allyNum}', True, "Gray")
        foeText = get_font(32, 'text').render(f'Foes: {foeNum}', True, "Gray")
        # Get Rectangles
        allyRect = allyText.get_rect()
        foeRect = foeText.get_rect()
        # Position Rectangles
        allyRect.move_ip(120, 120)
        foeRect.move_ip(120, 180)
        # Draw Rectangles
        WINDOW.blit(allyText, allyRect)
        WINDOW.blit(foeText, foeRect)
        pygame.display.update()
    
    # Reset Window after Battle
    WINDOW.fill("green")
    returnText = get_font(32, 'text').render('Press "z" to return', True, "Gray")
    returnRect = returnText.get_rect()
    returnRect.move_ip(520, 240)
    WINDOW.blit(returnText, returnRect)

    # Standard Loop
    while globals.frame == 'options':
        # Handle Events
        for event in pygame.event.get():
            # `X` Close button on window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle Input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    globals.save()
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_z:
                    globals.save()
                    globals.frame = 'title'
        pygame.display.update()

def crossroads():
    """Frame containing a navigable pseudo-random tree.
    
    This frame allows the user to navigate the tree. Press `UP`
    to navigate to the head node. Press `LEFT`/`Right` to go to
    the first or second bifurcation respectively.

    #==VARIABLES==#
    | floor is the current node
    """
    # Initialize Window
    pygame.display.set_caption(f"Project_Identidem/{globals.seed}/{globals.crossTree.index}")
    WINDOW.fill("black")
    
    # Crossroads Loop
    while globals.frame == 'cross':
        WINDOW.fill("black") # Clean frame
        floor = globals.crossTree # Establish the current index

        # Update Floor Info
        # Set Text
        floorText = get_font(32, 'text').render(f"Floor: {floor.depth + 1} / {floor.maxDepth + 1}",
                        True, "White")
        encounterText = get_font(32, 'text').render(f"{floor.content[0]}, {floor.content[1]}",
                        True, "White")
        # Get Rect
        floorRect = floorText.get_rect()
        encounterRect = encounterText.get_rect()
        # Move Rect
        floorRect.move_ip(520, 72)
        encounterRect.move_ip(520, 256)
        # Draw Rect
        WINDOW.blit(floorText, floorRect)
        WINDOW.blit(encounterText, encounterRect)
        # Handle Pygame events
        for event in pygame.event.get():
                # `X` Close button on window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Handle Input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        globals.save()
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    # Move Up
                    if event.key == pygame.K_UP and floor.depth != 0:
                        globals.crossTree = floor.head
                        pygame.display.set_caption(
                            f"Project_Identidem/{globals.seed}/{globals.crossTree.index}")
                    # Move Down Left
                    if event.key == pygame.K_LEFT and floor.depth != floor.maxDepth:
                        globals.crossTree = floor.tail[0]
                        pygame.display.set_caption(
                            f"Project_Identidem/{globals.seed}/{globals.crossTree.index}")
                    # Move Down Right
                    if event.key == pygame.K_RIGHT and floor.depth != floor.maxDepth:
                        globals.crossTree = floor.tail[1]
                        pygame.display.set_caption(
                            f"Project_Identidem/{globals.seed}/{globals.crossTree.index}")
                    if event.key == (pygame.K_z):
                        globals.save()
                        globals.frame = 'title'
        pygame.display.update()

#Run the code
if __name__ == "__main__":
    game()