import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Object collision !")

w = ((255,255,255))
b = ((0,0,255))
r = ((255,0,0))

class Shape(pygame.sprite.Sprite):
    def __init__(s,colr,x,y,width,height, dx, dy):
        super().__init__
        s.colr = colr
        s.rect = pygame.Rect(x,y,width,height)
        s.dx = dx
        s.dy = dy

    def draw(s):
        pygame.draw.rect(screen,s.colr,s.rect)

    def update(s):
        s.rect.x += s.dx
        s.rect.y += s.dy

class Rectangle(Shape):
    def __init__(s,colr,x,y,width,height, dx, dy):
        super().__init__(colr,x,y,width,height, dx, dy)

    def update(s):
        if s.rect.left < 0 or s.rect.right >SCREEN_WIDTH:
            s.dx *= -1
        if s.rect.top < 0 or s.rect.bottom > SCREEN_HEIGHT:
            s.dy *= -1
        s.rect.x += s.dx
        s.rect.y += s.dy

def display_collision_status(status):
    font = pygame.font.Font(None, 36)
    text = font.render(status, True,(17, 62,99))
    screen.blit(text,(300,50))

def main():
    b_rect = Rectangle(b,200,200,100,100,3,3)
    r_rect = Rectangle(r, 200,200,100,100,-2,2)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        b_rect.update()
        r_rect.update()

        screen.fill(w)
        b_rect.draw()
        r_rect.draw()

        is_collision = b_rect.rect.colliderect(r_rect.rect)

        if is_collision:
            display_collision_status("Collision Detected !")
        else:
            display_collision_status(" No Collision !")

        pygame.display.update()
        pygame.time.Clock().tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()