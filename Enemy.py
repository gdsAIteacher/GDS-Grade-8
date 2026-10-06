import pygame 
import math
import random
import os
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

assets_enemies = "assets/enemies"

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = self.load_images()
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
    def load_images(self):
        images = []
        for filename in os.listdir(assets_enemies):
            if filename.endswith(".png"):  
                image = pygame.image.load(os.path.join(assets_enemies, filename)).convert_alpha()
                images.append(image)
        return images
    
    def update(self, player_rect):
        dx = player_rect.x - self.rect.x
        dy = player_rect.y - self.rect.y                        
        dist = max(abs(dx), abs(dy))
        if dist != 0:
            self.rect.x += dx / dist
            self.rect.y += dy / dist

def main():
    pygame.display.set_caption("Space Hunter")
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    enemy = Enemy()
    enemy_group = pygame.sprite.Group()
    enemy_group.add(enemy)


    running = True
    clock = pygame.time.Clock()
    while running:
        
        screen.blit(BG, (0, 0))
        player_group.draw(screen)
        enemy_group.draw(screen)
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
        enemy_group.update(player.rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        clock.tick(60) 
    pygame.quit()

if __name__ == "__main__":
    main()