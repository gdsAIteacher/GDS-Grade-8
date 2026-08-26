import pygame
pygame.init()

height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse click event handling !!")
white = (255,255,255)
blue = (0,0,255)


def main():
    status = True
   
    
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                w.fill(white)
                pygame.draw.circle(w,blue,pos,20)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()