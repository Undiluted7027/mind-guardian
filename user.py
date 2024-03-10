import pygame 

#initialize pygame 
pygame.init() 

#create the screen
screen = pygame.display.set_mode((500, 500))

#Title and Icon 
pygame.display.set_caption("Mind Guardian")
#icon = pygame.image.load('user.png')
#pygame.display.set_icon

x = 50
y = 400
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10

images = pygame.image.load("player.png")
images = pygame.transform.scale(images, (100, 100))

#Game loop 
running = True 
while running:
    pygame.time.delay(50)
    screen.fill((255, 255, 255))
    screen.blit(images, dest = (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500-width-vel:
        x += vel
    if not(isJump):
        # comment this section for making the jump short & smooth
        # use **2 for jumps that potentially make the user fly super high lol (Edit: fixed in latest commit)
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500-height-vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2)*0.5*neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    pygame.display.update()

pygame.quit()