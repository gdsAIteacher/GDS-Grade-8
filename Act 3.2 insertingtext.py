import pygame
pygame.init()

win_h = 500
win_w = 500

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Inserting text")
f = pygame.font.Font(None, 36)
ts = f.render("Welcome Coders!!", True, (255, 0, 0))
white = ((255, 255, 255))

def main():
    while True:
        win.fill(white)
        win.blit(ts, (10, 50))
        pygame.display.flip()

if __name__ == "__main__":
    main()

