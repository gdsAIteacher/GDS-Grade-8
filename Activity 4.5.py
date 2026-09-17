import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball collision !")

w = ((255,255,255))


class Ball(pygame.sprite.Sprite):
    def __init__(s,img_path,x,y,dx,dy,width,height):
        super().__init__()
        s.img1 = pygame.image.load(img_path)
        s.img1 = pygame.transform.scale(s.img1,(width,height))
        s.rect = s.img1.get_rect(topleft = (x,y))
        s.dx = dx
        s.dy = dy

    def draw(s):
        screen.blit(s.img1,s.rect)

    def update(s):
        s.rect.x += s.dx
        s.rect.y += s.dy

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
    b1 =Ball(r"assets//redball.png", 200,200,3,3,80,80)
    b2 =Ball(r"assets//whtball.png", 400,300,-2,2,80,80)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        b1.update()
        b2.update()

        screen.fill(w)
        b1.draw()
        b2.draw()

        is_collision = b1.rect.colliderect(b2.rect)

        if is_collision:
            display_collision_status("Collision Detected !")
        else:
            display_collision_status(" No Collision !")

        pygame.display.update()
        pygame.time.Clock().tick(80)
    pygame.quit()

if __name__ == "__main__":
    main()