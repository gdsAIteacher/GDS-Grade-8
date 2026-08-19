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
        pygame.display.flip()

if __name__ == "__main__":
    main()