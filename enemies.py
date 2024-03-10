# import pygame module
import pygame

pygame.init()

# global
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mind Guardian 👼")
user_x = 0
user_y = 450
enemy_x = 450
enemy_y = 450
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10


images = (pygame.image.load("user.png"), pygame.image.load("enemy.png"))
images = [pygame.transform.scale(i, (50, 50)) for i in images]


class enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
    
    def draw(self, win):
        pass

    def move(self):
        pass



exit = False

while not exit:
    pygame.time.delay(50)
    win.fill((255, 255, 255))
    win.blit(images[0], dest = (user_x, user_y))
    win.blit(images[1], dest = (enemy_x, enemy_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and user_x > vel:
        user_x -= vel
    if keys[pygame.K_RIGHT] and user_x < 500-width-vel:
        user_x += vel
    if not(isJump):
        # comment this section for making the jump short & smooth
        # use **2 for jumps that potentially make the user fly super high lol (Edit: fixed in latest commit)
        if keys[pygame.K_UP] and user_y > vel:
            user_y -= vel
        if keys[pygame.K_DOWN] and user_y < 500-height-vel:
            user_y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            user_y -= (jumpCount ** 2)*0.5*neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    pygame.display.update()