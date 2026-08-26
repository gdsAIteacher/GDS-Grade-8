import pygame
pygame.init()
height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Inserting Text !")
white = (255,255,255)
img = pygame.image.load("assets\pupy.png")
s_img = pygame.transform.scale(img,(100,100))
surf = s_img.get_rect()
def main():
    status = True
    x_img = (width - surf.width)/2
    y_img = (height - surf.height)/2
    step = 10
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_img -=step
                if event.key == pygame.K_RIGHT:
                    x_img +=step
                if event.key == pygame.K_UP:
                    y_img -=step
                if event.key == pygame.K_DOWN:
                    y_img +=step
        w.fill(white)
        w.blit(s_img,(x_img,y_img))
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()