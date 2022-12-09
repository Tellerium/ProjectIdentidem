import globals, pygame, sys
from classes import *

pygame.init()
SCREEN = (1280, 720)
WINDOW = pygame.display.set_mode(SCREEN, pygame.SCALED)
ICON = pygame.image.load("./assets/images/test.ico")
pygame.display.set_caption("Project Identidem")
pygame.display.set_icon(ICON)

def get_font(size, fontKey):
    fontDict = {
        'title':'StarConstellation-87zn',
        'text':'Quicksand-Regular'
    }

    return pygame.font.Font(str("./assets/fonts/"+ fontDict[fontKey] + ".ttf"), size)

def game():
    while True:
        options()
        crossroads()
        title()

def title():
    #Initialize Window
    pygame.display.set_caption("Project Identidem")
    WINDOW.fill("black")
    onTitle = True
    #Initialize Title & Instructions
    #Set Text
    titleText = get_font(64, 'title').render("Identidem", True, 'Purple')
    instructionText = get_font(32, 'text').render("UP/DOWN To Select ", True, "White")
    #Get Rectangles
    titleRect = titleText.get_rect()
    instructionRect = instructionText.get_rect()
    #Position Rectangles
    titleRect.move_ip(480, 72)
    instructionRect.move_ip(8, 680)
    #Draw Rectangles
    WINDOW.blit(titleText, titleRect)
    WINDOW.blit(instructionText, instructionRect)

    #Initialize Buttons
    #Text Dictionaries
    textIndex = 0
    indexChanged = False
    textDict = {
        '0':'New Loop',
        '1':'Resume Loop',
        '2':'Options',
        '3':'Give Up'
    }
    textPos = {
        '0':(SCREEN[0]/2, 144),
        '1':(SCREEN[0]/2, 288),
        '2':(SCREEN[0]/2, 432),
        '3':(SCREEN[0]/2, 576)
    }
    #Set Text
    newText = get_font(32, 'text').render(textDict.get('0'), True, "Gray")
    loadText = get_font(32, 'text').render(textDict.get('1'), True, "Gray")
    settingsText = get_font(32, 'text').render(textDict.get('2'), True, "Gray")
    exitText = get_font(32, 'text').render(textDict.get('3'), True, "Gray")
    #Get Rectangles
    newRect = newText.get_rect()
    loadRect = loadText.get_rect()
    settingsRect = settingsText.get_rect()
    exitRect = exitText.get_rect()
    #Position Rectangles
    newRect.move_ip(textPos.get('0'))
    loadRect.move_ip(textPos.get('1'))
    settingsRect.move_ip(textPos.get('2'))
    exitRect.move_ip(textPos.get('3'))
    #Draw Rectangles
    WINDOW.blit(newText, newRect)
    WINDOW.blit(loadText, loadRect)
    WINDOW.blit(settingsText, settingsRect)
    WINDOW.blit(exitText, exitRect)

    #Selected Text
    selectedText = get_font(32, 'text').render(textDict.get(str(textIndex)), True, "Blue")
    selectedRect = selectedText.get_rect()
    selectedRect.move_ip(textPos.get(str(textIndex)))
    WINDOW.blit(selectedText, selectedRect)

    #Perform Title Screen Processing
    while globals.frame == 'title':
    #Update Selected Text
        if indexChanged != -1:
            selectedText = get_font(32, 'text').render(textDict.get(str(indexChanged)), True, "Gray")
            WINDOW.blit(selectedText, selectedRect)
            indexChanged = -1
            selectedText = get_font(32, 'text').render(textDict.get(str(textIndex)), True, "Blue" if textIndex != 3 else "Red")
            selectedRect = selectedText.get_rect()
            selectedRect.move_ip(textPos.get(str(textIndex)))
            WINDOW.blit(selectedText, selectedRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_DOWN:
                    #Update Index
                    indexChanged = textIndex
                    textIndex = (textIndex + 1) % 4
                if event.key == pygame.K_UP:
                    #Update Index
                    indexChanged = textIndex
                    textIndex = (textIndex - 1) % 4
                if event.key == (pygame.K_BACKSPACE):
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
    globals.seed = globals.newSeed()
    globals.frame = 'cross'

def load_Game():
    globals.frame = 'cross'

def options():
    pygame.display.set_caption('Options')
    WINDOW.fill("green")
    
    while globals.frame == 'options':
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    if event.key == (pygame.K_z):
                        globals.frame = 'title'
        
        pygame.display.update()

def crossroads():
    pygame.display.set_caption(str(globals.seed))
    WINDOW.fill("pink")

    while globals.frame == 'cross':
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_f:
                        pygame.display.toggle_fullscreen()
                    if event.key == (pygame.K_z):
                        globals.frame = 'title'
    
        pygame.display.update()

if __name__ == '__main__':
    globals.init()
    game()
    
