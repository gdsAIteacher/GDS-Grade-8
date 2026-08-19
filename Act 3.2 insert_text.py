import pygame
pygame.init()
height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Inserting Text !")
white = (255,255,255)
blue = (0,0,255)
f = pygame.font.Font(None,36)
surf = f.render("WELCOME TO PYGAME !",True,blue)
def main():
    while True:
        w.fill(white)
        w.blit(surf,(70,250))
        pygame.display.update() 
if __name__ == "__main__":
    main()