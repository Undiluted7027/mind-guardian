# import pygame module
import pygame

pygame.init()

# global
win = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Mind Guardian 👼")


USER_IMG = pygame.image.load("user.png")
ST_ENEMY_IMG = pygame.image.load("enemy.png")
USER_IMG = pygame.transform.scale(USER_IMG, (80, 80))
ST_ENEMY_IMG = pygame.transform.scale(ST_ENEMY_IMG, (100, 100))
backdrop = pygame.image.load("images/backdrop4.jpg")
backdrop = pygame.transform.scale(backdrop, (600, 480))
walkLeftRetro = [pygame.image.load('trial/L1.png'), pygame.image.load('trial/L2.png'), pygame.image.load('trial/L3.png')]
walkRightRetro = [pygame.image.load('trial/R1.png'), pygame.image.load('trial/R2.png'), pygame.image.load('trial/R3.png')]
walkRightRetro = [pygame.transform.scale(i, (65, 65)) for i in walkRightRetro]
walkLeftRetro = [pygame.transform.scale(i, (65, 65)) for i in walkLeftRetro]


USER_X = 0
USER_Y = 250
ENEMY_X = 350
ENEMY_Y = 220
WIDTH = 40
HEIGHT = 60
V = 5
isJump = False
jumpCount = 10
LEFT = False
RIGHT = False
walkCount = 0



clock = pygame.time.Clock()

exit = False

def redrawScreen():
    global walkCount
    # win.fill((255, 255, 255)) # debugger
    win.blit(backdrop, (0, 0))

    if walkCount + 1 >= 9:
        walkCount = 0
    if LEFT:
        win.blit(walkLeftRetro[walkCount//3], (USER_X, USER_Y))
        walkCount += 1
    elif RIGHT:
        win.blit(walkRightRetro[walkCount//3], (USER_X, USER_Y))
        walkCount += 1
    else:
        win.blit(USER_IMG, (USER_X, USER_Y))

    win.blit(ST_ENEMY_IMG, dest = (ENEMY_X, ENEMY_Y))
    pygame.display.update()


class enemy(object):
    walkRight = [pygame.image.load("images/R1E.png"),pygame.image.load("images/R1E.png"),pygame.image.load("images/R1E.png"),]

# LOOP
while not exit:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and USER_X > V:
        USER_X -= V
        LEFT = True
        RIGHT = False
    elif keys[pygame.K_RIGHT] and USER_X < 500-WIDTH-V:
        USER_X += V
        RIGHT = True
        LEFT = False
    else:
        RIGHT = False
        LEFT = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            RIGHT = False
            LEFT = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            USER_Y -= (jumpCount * abs(jumpCount)) * 0.25
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawScreen()

pygame.quit()