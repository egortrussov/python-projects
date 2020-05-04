import pygame

pygame.init()

screen = pygame.display.set_mode([400, 450])

pygame.display.set_caption('Crappy game')


running = True

class Node():
    def __init__(self, x, y):
        self.x  = x
        self.y = y

playerX = 7
playerY = 7
gridSize = 20
tileC = 20
appleX = 7
appleY = 2
vx = 0
vy = 0
trail = []
tail = 5
score = 0

# def drawWindow():
#     pygame.draw.rect(screen, [255, 0, 0], [0, 0, 400, 400])
#     pygame.draw.rect(screen, [0, 0, 0], [5, 5, 390, 390])

#     if (playerX < 0):
#         playerX = tileC - 1
#     if (playerX > tileC - 1):
#         playerX = 0
#     if (playerY < 0):
#         playerY = tileC - 1
#     if (playerY > tileC - 1):
#         playerY = 0

#     for node in trail:
#         pygame.draw.rect(screen, [255, 0, 0], [
#             node.x * gridSize,
#             node.y * gridSize,
#             gridSize - 2,
#             gridSize - 2
#         ])
    
#     trail.push(Node(playerX, playerY))

#     while (len(trail) > tail):
#         trail.pop(0)
    
    
#     pygame.display.update()

pygame.display.flip()

while (running):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_UP]):
        vy = -1
        vx = 0
    if (keys[pygame.K_DOWN]):
        vy = 1
        vx = 0
    if (keys[pygame.K_LEFT]):
        vx = -1
        vy = 0
    if (keys[pygame.K_RIGHT]):
        vx = 1
        vy = 0

    playerX += vx
    playerY += vy    
    
    pygame.draw.rect(screen, [255, 0, 0], [0, 0, 400, 400])
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 390, 390])

    if (playerX < 0):
        playerX = tileC - 1
    if (playerX > tileC - 1):
        playerX = 0
    if (playerY < 0):
        playerY = tileC - 1
    if (playerY > tileC - 1):
        playerY = 0

    for node in trail:
        pygame.draw.rect(screen, [255, 0, 0], [
            node.x * gridSize,
            node.y * gridSize,
            gridSize - 2,
            gridSize - 2
        ])
    
    trail.append(Node(playerX, playerY))

    while (len(trail) > tail):
        trail.pop(0)
    
    
    pygame.display.update()

    # drawWindow()