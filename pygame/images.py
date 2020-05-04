import pygame
import time

pygame.init()

screen = pygame.display.set_mode([600, 700])

bg = pygame.image.load('image.jpg').convert()
bg_rect = bg.get_rect(center=(200, 150))
bg1 = pygame.image.load('image2.jpg').convert()
bg1_rect = bg1.get_rect(center=(300, 280))

screen.blit(bg, bg_rect)

prev_change = time.perf_counter()
curr_img = 1

pygame.display.update()

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            pygame.quit()
    curr_time = time.perf_counter()
    if (curr_time - prev_change >= 1): 
        prev_change = curr_time 
        print(curr_img)
        if (curr_img == 1): 
            screen.blit(bg1, bg1_rect)
            curr_img = 2
        else:
            screen.blit(bg, bg_rect)
            curr_img = 1
        pygame.display.update()