import globals, pygame, sys
from classes import *

pygame.init()
WINDOW = pygame.display.set_mode((1280, 720), pygame.SCALED)
ICON = pygame.image.load("./assets/images/test.ico")
pygame.display.set_caption("Project Identidem")
pygame.display.set_icon(ICON)

def get_font(size, fontKey):
    fontDict = {
        'title':'StarConstellation-87zn',
        'text':'Quicksand-Regular'
        }

    return pygame.font.Font(str("./assets/fonts/"+ fontDict[fontKey] + ".ttf"), size)

def title():
    pygame.display.set_caption("Project Identidem")
    WINDOW.fill("black")

    while True:
        MENU_TEXT = get_font(64, 'title').render("Identidem", True, 'Purple')
        WINDOW.blit(MENU_TEXT, (480, 72))

        INSTRUCTION_TEXT = get_font(32, 'text').render("UP/DOWN To Select ", True, "White")
        WINDOW.blit(INSTRUCTION_TEXT, (16, 672))

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

        pygame.display.update()

if __name__ == '__main__':
    globals.init()
    title()
    
