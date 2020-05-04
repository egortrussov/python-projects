import pygame

screen = pygame.display.set_mode([1200, 700])

done = True

screen.fill([255,255,255])


pygame.draw.rect(screen, [125, 165, 112], [20, 40, 25, 15])
pygame.draw.rect(screen, [125, 165, 112], [45, 25, 20, 30])
pygame.draw.rect(screen, [125, 195, 212], [25, 25, 5, 15])
pygame.draw.rect(screen, [125, 195, 212], [50, 30, 10, 10])
pygame.draw.rect(screen, [125, 195, 212], [70, 30, 45, 25])

pygame.draw.circle(screen, [93,68,255],[30,60], 5, 0)
pygame.draw.circle(screen, [93,68,255],[55,60], 5, 0)
pygame.draw.circle(screen, [93,68,255],[75,60], 5, 0)
pygame.draw.circle(screen, [93,68,255],[100,60], 5, 0)
pygame.draw.circle(screen, [93,68,255],[110,60], 5, 0)
pygame.draw.circle(screen, [93,68,255],[110,60], 5, 0)

pygame.draw.circle(screen, [93,68,255],[30,20], 2, 0)
pygame.draw.circle(screen, [93,68,255],[35,15], 4, 0)
pygame.draw.circle(screen, [93,68,255],[45,10], 5, 0)


pygame.display.flip()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
