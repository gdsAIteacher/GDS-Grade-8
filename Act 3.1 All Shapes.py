import pygame
pygame.init()

win_h = 500
win_w = 500

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Drawing Shapes")

white = ((255, 255, 255))
red   = ((255, 0, 0))
blue = ((0, 0, 255))
yellow = ((255, 255, 0))


def main():
    while True:
        win.fill(white)
        pygame.draw.rect(win, red,(50,50, 200, 100))
        pygame.draw.circle(win, blue, (150, 200), 50)
        pygame.draw.line(win, yellow, (50, 300), (250, 300), 5) 

        pygame.display.flip()

if __name__ == "__main__":
    main()

