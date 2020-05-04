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

playerX = 10
playerY = 10
gridSize = 20
tileC = 20
appleX = 10
appleY = 7
vx = 0
vy = 0
trail = []
tail = 5
score = 0
direction = ''
isPlaying = True
isGameOver = False
isNextLevelMenu = False
isFinishGameMenu = False
level = 1
goalScore = 1
levelNum = 3

def reset():
    global playerX; 
    global playerY
    global appleX
    global appleY 
    global trail 
    global tail 
    global score 
    global vx 
    global vy 
    global isPlaying
    global isGameOver 
    
    playerX = 10
    playerY = 10
    appleX = 10
    appleY = 7
    trail = []
    tail = 5
    vx = 0
    vy = 0
    score = 0
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
    pygame.draw.rect(screen, [0, 0, 255], [70, 150, 260, 100])
    pygame.draw.rect(screen, [0, 0, 0], [75, 155, 250, 90])
    gameOverText = font1.render('Game over, noob!', 1, (255, 255, 255))
    restertText = font.render('Press R to restart', 1, (255, 255, 255))
    screen.blit(gameOverText, (105, 165))
    screen.blit(restertText, (130, 205))

def drawNextLevelMenu():
    global level

    pygame.draw.rect(screen, [0, 255, 0], [70, 60, 260, 300])
    pygame.draw.rect(screen, [0, 0, 0], [75, 65, 250, 290])
    gameOverText = font1.render('Congrats!', 1, (255, 255, 255))
    passedLevelText = font.render('You have passed level ' + str(level) , 1, (255, 255, 255))
    restertText = font.render('Press Space to continue!', 1, (255, 255, 255))
    screen.blit(gameOverText, (145, 85))
    screen.blit(passedLevelText, (100, 115))
    screen.blit(restertText, (100, 300))

def drawFinishGameMenu():
    pygame.draw.rect(screen, [0, 255, 0], [70, 60, 260, 300])
    pygame.draw.rect(screen, [0, 0, 0], [75, 65, 250, 290])
    gameOverText = font1.render('Congrats!', 1, (255, 255, 255))
    passedLevelText = font.render('You completed the game!', 1, (255, 255, 255))
    restertText = font.render('Press Space to restart!', 1, (255, 255, 255))
    screen.blit(gameOverText, (145, 85))
    screen.blit(passedLevelText, (100, 115))
    screen.blit(restertText, (100, 300))

pygame.display.flip()

while (running):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()

    if (isGameOver and keys[pygame.K_r]):
        reset()
        print(playerX)
        isGameOver = False
        isPlaying = True
    
    if (isNextLevelMenu and keys[pygame.K_SPACE]):
        reset()
        level += 1
        isNextLevelMenu = False
        isPlaying = True
    
    if (isFinishGameMenu and keys[pygame.K_SPACE]):
        reset()
        level = 1
        isFinishGameMenu = False
        isPlaying = True

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
    
    if (score >= goalScore):
        isPlaying = False 
        if (level == levelNum):
            isFinishGameMenu = True
        else:
            isNextLevelMenu = True
    
    if isPlaying:
        playerX += vx
        playerY += vy 
    
    pygame.draw.rect(screen, [0, 0, 0], [0, 0, 400, 500])
    pygame.draw.rect(screen, [255, 0, 0], [0, 0, 400, 400])
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 390, 390])

    scoreText = font.render(('Score: ' + str(score) + ' / ' + str(goalScore)), 1, (255, 255, 255))
    levelText = font.render(('Level: ' + str(level)), 1, (255, 255, 255))
    screen.blit(scoreText, (10, 410))
    screen.blit(levelText, (320, 410))

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
        nodeColor = [255, 0, 0]
        if (index == len(trail)):
            nodeColor = [255, 255, 255]
        pygame.draw.rect(screen, nodeColor, [
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
    
    if (isNextLevelMenu):
        drawNextLevelMenu()
    
    if (isFinishGameMenu):
        drawFinishGameMenu()
    
    
    pygame.display.update()

    # drawWindow()