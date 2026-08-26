import pygame
pygame.init()

win_h = 500
win_w = 500

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Draw Circle at Mouse pointer")

wht = ((255, 255, 255))
blu = ((0, 0, 255))

def main():
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                win.fill(wht)
                pygame.draw.circle(win, blu, pos, 20)
                
        pygame.display.flip()
        
        
    pygame.quit()

if __name__ == "__main__":
    main()

