import pygame
import math
pygame.init()

win_h = 500
win_w = 500

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Inserting Picture")
img = pygame.image.load("C:\Users\91908\OneDrive\Desktop\GDS\Grade-8\Computer Science\assets\images\dog.png")
img_rect = img.get_rect()
white = ((255, 255, 255))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x_mouse, y_mouse = pygame.mouse.get_pos()
        dx = x_mouse - win_w/2
        dy = y_mouse - win_h/2
        angle = math.degrees(math.atan2(-dy, dx))
        rot_img = pygame.transform.rotate(img, angle)
        r_rotimg = rot_img.get_rect(center=(win_w/2, win_h/2))  



        win.fill(white)
        win.blit(rot_img, r_rotimg.topleft)
        pygame.display.flip()

if __name__ == "__main__":
    main()

