import pygame
import math

pygame.init()
height = 500
width = 500
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating an image with the mouse!!")
white = (255,255,255)
blue = (0,0,255)

img = pygame.image.load("assets\pupy.png")
s_img = pygame.transform.scale(img,(100,100))
surf = s_img.get_rect()

def main():
    status = True
   
    
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
        ximg, yimg = pygame.mouse.get_pos()
        dx = ximg - width / 2    
        dy = yimg - height / 2
        angle = math.degrees(math.atan2(-dy,dx))
        rimg = pygame.transform.rotate(s_img, angle)
        rot_rect = rimg.get_rect(center = (width/2, height/2))
        w.fill(white)
        w.blit(rimg,rot_rect)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()