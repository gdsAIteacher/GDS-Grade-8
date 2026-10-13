import pygame 
import math
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Loading Images
background = pygame.image.load(r"assets\background-black.png")
BG = pygame.transform.scale(background,(SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = pygame.image.load(r"assets/pixel_ship_yellow.png")
player_image = pygame.transform.rotate(player_img, -90)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = player_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rotate()
    
    def rotate(self):
        #retrieves the mouse cursor's position on the screen
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #Calculates the relative distance between the player sprite's center 
        #and the mouse cursor’s position.
        rel_x = mouse_x - self.rect.centerx
        rel_y =  mouse_y - self.rect.centery

        angle = math.degrees(-math.atan2(rel_y, rel_x))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

def main():
    pygame.display.set_caption("Space Hunter")
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    running = True
    clock = pygame.time.Clock()
    while running:
        
        screen.blit(BG, (0, 0))
        player_group.draw(screen)
        # Player Movement Event Handling along with detecting boundary collision
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            dx = -5
        if keys[pygame.K_RIGHT] and player.rect.right < SCREEN_WIDTH:
            dx = 5
        if keys[pygame.K_UP] and player.rect.top > 0:
            dy = -5
        if keys[pygame.K_DOWN] and player.rect.bottom < SCREEN_HEIGHT:
            dy = 5
        player_group.update(dx, dy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        clock.tick(60) 
    pygame.quit()

if __name__ == "__main__":
    main()