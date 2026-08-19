import pygame
pygame.init()
height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Inserting Text !")
white = (255,255,255)
img = pygame.image.load("assets\pupy.png")
def main():
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
        w.fill(white)
        w.blit(img,(70,70))
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()