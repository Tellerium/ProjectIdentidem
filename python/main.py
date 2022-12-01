import globals, pygame, sys
from classes import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Project Idetidem")

#BG = pygame.image.load('./assets/titleBG.png')

def get_font(size, fontKey):
    fontDict = {
        'title':'StarConstellation-87zn',
        'text':'Quicksand-Regular'
        }

    return pygame.font.Font(str("./assets/fonts/"+ fontDict[fontKey] + ".ttf"), size)

def title():
    pygame.display.set_caption("Project Identidem")
    SCREEN.fill("black")

    while True:
        #SCREEN.blit(BG, (0, 0))

        MENU_TEXT = get_font(64, 'title').render("Identidem", True, 'Purple')
        MENU_TEXT_SHADOW = get_font(65, 'title').render("Identidem", True, 'White')
        SCREEN.blit(MENU_TEXT_SHADOW, (478, 72))
        SCREEN.blit(MENU_TEXT, (480, 72))

        INSTRUCTION_TEXT = get_font(32, 'text').render("UP/DOWN To Select", True, "White")
        SCREEN.blit(INSTRUCTION_TEXT, (16, 672))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    globals.init()
    title()
    
