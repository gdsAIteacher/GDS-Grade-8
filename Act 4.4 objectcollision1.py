import pygame
pygame.init()

win_h = 600
win_w = 800

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("object collision")
wht = ((255, 255, 255))
red = ((255, 0, 0))
blu = ((0, 0, 255))

class Shape(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, dx, dy):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.dx = dx
        self.dy = dy

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

class Rectangle(Shape):
    def __init__(self, color, x, y, width, height, dx, dy):
        super().__init__(color, x, y, width, height, dx, dy)

    def update(self):
        if self.rect.left < 0 or self.rect.right > win_w:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > win_h:
            self.dy *= -1
    
        self.rect.x += self.dx
        self.rect.y += self.dy

def col_status(status):
    font = pygame.font.Font(None, 36)
    text = font.render(status, True, (17, 62, 99))
    win.blit(text, (300, 400))

def main():
    rd = Rectangle(red, 200, 200, 100, 100, 3, 3)
    blue = Rectangle(blu, 400, 200, 100, 100, -2, 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rd.update()
        blue.update()
        win.fill(wht)
        rd.draw()
        blue.draw()

        is_collision = blue.rect.colliderect(rd.rect)
        if is_collision:
            col_status("Collision Detected!")
        else:
            col_status("No Collision")
        pygame.display.update()

        pygame.time.Clock().tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
