import pygame
pygame.init()

win_h = 500
win_w = 500

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Inserting Picture")
img = pygame.image.load("asset\\img1.png")
scalimg = pygame.transform.scale(img, (100, 100))
img_rect = scalimg.get_rect()

white = ((255, 255, 255))

def main():
    status = True
    imgx = (win_w - img_rect.width) // 2
    imgy = (win_h - img_rect.height) // 2
    speed = 50
    while status:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    imgx -= speed
                elif event.key == pygame.K_RIGHT:
                    imgx += speed
                elif event.key == pygame.K_UP:
                    imgy -= speed
                elif event.key == pygame.K_DOWN:
                    imgy += speed
            if imgx < 0:
                imgx = 0
            if imgx > win_w - img_rect.width:
                imgx = win_w - img_rect.width
            if imgy < 0:
                imgy = 0
            if imgy > win_h - img_rect.height:
                imgy = win_h - img_rect.height


        win.fill(white)
        win.blit(scalimg, (imgx, imgy))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()

