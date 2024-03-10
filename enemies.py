import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mind Guardian 👼")

walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), ...]
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), ...]

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

    def draw(self):  # Removed self.win from parameters
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))  # Changed to self.x, self.y
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))  # Changed to self.x, self.y
            self.walkCount += 1
        else:
            win.blit(images[0], (self.x, self.y))  # Changed to self.x, self.y


user_x = 0
user_y = 350
enemy_x = 350
enemy_y = 350
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
LEFT = False
RIGHT = False
walkCount = 0



clock = pygame.time.Clock()

exit = False

def redrawScreen():  # Removed unused images parameter
    win.blit(backdrop, (0, 0))
    man.draw()  # Changed to call draw on the instance
    pygame.display.update()


class enemy(object):
    walkRight = [pygame.image.load("images/R1E.png"),pygame.image.load("images/R1E.png"),pygame.image.load("images/R1E.png"),]

# LOOP

man = player(300, 410, 64, 64)
while not exit:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.user_x > man.vel:
        man.user_x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.user_x < 500-man.width-man.vel:
        man.user_x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.user_y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else: 
            man.jumpCount = 10
            man.isJump = False

    redrawScreen()

pygame.quit()