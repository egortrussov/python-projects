import pygame 
import math

pygame.init()
screen = pygame.display.set_mode([500, 500])

pygame.display.set_caption('game')

walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'), pygame.image.load('right_3.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

x = 50
y = 425
width = 40
height = 60 
speed = 5
lastMove = "right"

class bullet():
    def __init__(self, x, y, r, color, facing):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.facing = facing
        self.vel = facing * 16
    def draw(self, win):
        pygame.draw.circle(win, self.color, [self.x, self.y], self.r)

def drawWindow ():
    global animCount
    win.blit(bg,(0,0))
    if animCount +1>=30:
        animCount=0
    if left:
        win.blit(walkLeft[animCount//5],(x,y))
        animCount+=1
    elif right:
        win.blit(walkright[animCount//5],(x,y))
        animCount+=1
    else:
        win.blit(playerStand,(x,y))
    for b in bullets:
        b.draw(screen)

    pygame.display.update()

bullets = []

isJump = False 
jumpCount = 10

running = True 
while (running):
    pygame.time.delay(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    for b in bullets:
        if b.x < 500 and b.x > 0:
            b.x += b.vel 
        else:
            bullets.pop(bullets.index(b))
    
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_f]):
        if len(bullets) < 10:
            if lastMove == "right":
                facing = 1
            else:
                facing = -1
            bullets.append(bullet(round(x + width // 2), round(y + height // 2), 8, (255, 0, 0), facing))

    if (keys[pygame.K_LEFT] and x > 5):
        lastMove = "left"
        x -= speed
    if (keys[pygame.K_RIGHT] and x < 500 - 5 - width):
        lastMove = "right"
        x += speed

    if not isJump:
        # if (keys[pygame.K_UP] and y > 5):
        #     y -= speed
        # if (keys[pygame.K_DOWN]  and y < 500 - 5 - height):
        #     y += speed
        if (keys[pygame.K_SPACE]): 
            isJump = True
    else:
        if jumpCount >= -10:
            if (jumpCount > 0):
                y -= (jumpCount ** 2) / 2
            else: 
                y += (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False 
            jumpCount = 10
    
    drawWindow()

pygame.quit()