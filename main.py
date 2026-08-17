import pygame
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HIGHT = 500
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("My First Game")
white=(255,255,255)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,0,255)
font = pygame.font.Font(None, 36)
text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(white)
        pygame.draw.rect(window, yellow, (100, 100, 30, 30))
        pygame.draw.circle(window, green, (250, 250), 50)
        pygame.draw.line(window, blue, (300, 300), (400, 400), 5)
        pygame.display.flip()
if __name__ == "__main__":
    main()