import pygame
import math 
import random

pygame.init()

screen = pygame.display.set_mode([400, 450])

pygame.display.set_caption('Crappy game')

font = pygame.font.Font(None, 24)
font1 = pygame.font.Font(None, 34)

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
tail = 10
score = 0
direction = ''
isPlaying = True
isGameOver = False

def drawApple():
    pygame.draw.rect(screen, [255, 0, 0], [
        appleX * gridSize,
        appleY * gridSize,
        gridSize - 2,
        gridSize - 2
    ])

def drawGameOverMenu():
    pygame.draw.rect(screen, [0, 255, 0], [70, 150, 260, 100])
    pygame.draw.rect(screen, [0, 0, 0], [75, 155, 250, 90])
    gameOverText = font1.render('Game over, noob!', 1, (255, 255, 255))
    restertText = font.render('Press R to restart', 1, (255, 255, 255))
    screen.blit(gameOverText, (105, 165))
    screen.blit(restertText, (130, 205))

pygame.display.flip()

while (running):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()

    if (isPlaying):

        if (keys[pygame.K_UP] and direction != 'down'):
            direction = 'up'
            vy = -1
            vx = 0
        if (keys[pygame.K_DOWN] and direction != 'up'):
            direction = 'down'
            vy = 1
            vx = 0
        if (keys[pygame.K_LEFT] and direction != 'right'):
            direction = 'left'
            vx = -1
            vy = 0
        if (keys[pygame.K_RIGHT] and direction != 'left'):
            direction = 'right'
            vx = 1
            vy = 0
    
    if isPlaying:
        playerX += vx
        playerY += vy 
    
    pygame.draw.rect(screen, [0, 0, 0], [0, 0, 400, 500])
    pygame.draw.rect(screen, [255, 0, 0], [0, 0, 400, 400])
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 390, 390])

    scoreText = font.render(('Score: ' + str(score)), 1, (255, 255, 255))
    screen.blit(scoreText, (10, 410))

    if (playerX < 0):
        playerX = tileC - 1
    if (playerX > tileC - 1):
        playerX = 0
    if (playerY < 0):
        playerY = tileC - 1
    if (playerY > tileC - 1):
        playerY = 0

    index = 0

    for node in trail:
        index += 1
        pygame.draw.rect(screen, [255, 0, 0], [
            node.x * gridSize,
            node.y * gridSize,
            gridSize - 2,
            gridSize - 2
        ])
        if (not vx and not vy):
            continue
        if (playerX == node.x and playerY == node.y and index != len(trail) and len(trail) > 0):
            print('HHH')
            isPlaying = False
            isGameOver = True
        
    
    if not isPlaying:
        vx = 0
        vy = 0
    
    if isPlaying:
    
        trail.append(Node(playerX, playerY))

        while (len(trail) > tail):
            trail.pop(0)
        
        if (appleX == playerX and appleY == playerY):
            tail += 1
            score += 1
            
            isAppleCoordFound = False 
            while (not isAppleCoordFound):
                appleX = random.randint(1, tileC - 1)
                appleY = random.randint(1, tileC - 1)

                isCorrect = True

                for node in trail:
                    if (node.x == appleX and node.y == appleY):
                        isCorrect = False 
                        break
                isAppleCoordFound = isCorrect
            
        drawApple()
    
    if (isGameOver):
        drawGameOverMenu()
    
    
    pygame.display.update()

    # drawWindow()