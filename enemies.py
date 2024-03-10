import pygame

pygame.init()

win = pygame.display.set_mode((680, 500))
pygame.display.set_caption("Mind Guardian 👼")

ST_ENEMY_IMG = pygame.image.load('enemy.png')
USER_IMG = pygame.image.load('user.png')
USER_IMG = pygame.transform.scale(USER_IMG, (100, 100))
BACKDROP = pygame.image.load('images/backdrop4.jpg')
BACKDROP = pygame.transform.scale(BACKDROP, (680, 500))
walkLeft = [pygame.image.load('trial/L1.png'), pygame.image.load('trial/L2.png'),pygame.image.load('trial/L3.png')]
walkRight = [pygame.image.load('trial/R1.png'), pygame.image.load('trial/R2.png'), pygame.image.load('trial/R3.png')]
walkLeft = [pygame.transform.scale(i, (80, 80)) for i in walkLeft]
walkRight = [pygame.transform.scale(i, (80, 80)) for i in walkRight]


user_x = 0
user_y = 350
enemy_x = 350
enemy_y = 150
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
LEFT = False
RIGHT = False
walkCount = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x  # Renamed from user_x to x
        self.y = y  # Renamed from user_y to y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self):  # Removed self.win from parameters
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y)) 
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))  
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))

class shoot(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) 


clock = pygame.time.Clock()

exit = False

def redrawScreen():  # Removed unused images parameter
    win.blit(BACKDROP, (0, 0))
    man.draw()  # Changed to call draw on the instance
    for bullet in bullets:
        bullet.draw()
    pygame.display.update()


class enemy(object):
    enemy_walk_left = [pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]
    enemy_walk_right = [pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]


# LOOP

man = player(250, 250, 80, 80)
bullets = []
while not exit:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel 
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(shoot(round(man.x + man.width // 2),round(man.y + man.height // 2), 6, (0,0,0), facing))
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500-man.width-man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.25
            man.jumpCount -= 1
        else: 
            man.jumpCount = 10
            man.isJump = False

    redrawScreen()

pygame.quit()