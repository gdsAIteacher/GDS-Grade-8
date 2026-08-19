import pygame
pygame.init()

height = 500
width = 500
w = pygame.display.set_mode((width, height))

def main():
    while True:
        pygame.display.flip()

if __name__ == "__main__":
    main()