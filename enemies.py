# import pygame module
import pygame

pygame.init()

# global
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mind Guardian 👼")

walkLeft = [pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png'),]

walkRight = [pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png'),]

user_x = 0
user_y = 350
enemy_x = 350
enemy_y = 350
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

images = (pygame.image.load("user.png"), pygame.image.load("enemy.png"))
images = [pygame.transform.scale(i, (100, 100)) for i in images]
backdrop = pygame.image.load("images/backdrop.png")
backdrop = pygame.transform.scale(backdrop, (640, 500))



exit = False

def redrawScreen(images):
    global walkCount
    # win.fill((255, 255, 255))
    win.blit(backdrop, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        win.blit(walkLeft[walkCount//3], (user_x, user_y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (user_x, user_y))
        walkCount += 1
    else:
        win.blit(images[0], (user_x, user_y))

    # win.blit(images[0], dest = (user_x, user_y))
    # win.blit(images[1], dest = (enemy_x, enemy_y))

    pygame.display.update()

# LOOP

while not exit:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and user_x > vel:
        user_x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and user_x < 500-width-vel:
        user_x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            user_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawScreen(images)

pygame.quit()
    
    