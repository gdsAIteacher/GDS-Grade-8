import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Collision Detection")

# Colors
WHITE = (255, 255, 255)

# Base class for images
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, dx, dy, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height)) # Resize the image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx = dx
        self.dy = dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        # Move the ball
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for boundary collision and reverse direction if necessary
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy *= -1

# Function to display collision status text
def display_collision_status(status):
    font = pygame.font.Font(None, 36)
    text = font.render(status, True, (255, 0, 0))
    screen.blit(text, (250, 50))

def main():
    # Create ball objects with images and specify the size (width, height)
    ball1 = Ball("assets/ball1.png", 200, 200, 3, 3, 80, 80) # 80x80 size
    ball2 = Ball("assets/ball2.png", 400, 300, -2, 2, 80, 80) # 80x80 size

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update ball positions
        ball1.update()
        ball2.update()

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the balls
        ball1.draw(screen)
        ball2.draw(screen)

        # Check for collision between balls
        if ball1.rect.colliderect(ball2.rect):
            display_collision_status("Ball Collision Detected")
        else:
            display_collision_status("No Ball Collision")

        # Update the display
        pygame.display.update()

        # Control frame rate
        pygame.time.Clock().tick(60)

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()
