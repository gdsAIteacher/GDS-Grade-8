import pygame
pygame.init()

height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Window with white BG")
white = (255,255,255)

def main():
    while True:
        w.fill(white)
        pygame.draw.rect(w,(0,0,255), (100, 50, 100, 50))
        pygame.draw.circle(w, (255,255,0),(200,350), 50)
        pygame.draw.line(w,(255,0,0),(250,250),(400,400),3)
        pygame.display.flip()

if __name__ == "__main__":
    main()