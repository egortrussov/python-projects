import pygame
screen = pygame.display.set_mode([640, 480])
done = True
screen.fill([255,255,255])
pygame.draw.circle(screen, [93,68,255],[170,60], 50, 0)
pygame.draw.rect(screen, [255,0,0], [80, 130, 180, 180], 0)
pygame.draw.line (screen, [0,255,33], [50, 100], [50, 300],5)
pygame.display.flip()
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
