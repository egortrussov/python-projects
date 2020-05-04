import pygame

window = pygame.display.set_mode([400, 400])
pygame.display.set_caption('Hello, pygame')

screen = pygame.Surface([400, 400])

done = True

while done:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            done
    
    screen.fill([255, 0, 0])

    window.blit(screen, [0, 0])
    pygame.display.flip()