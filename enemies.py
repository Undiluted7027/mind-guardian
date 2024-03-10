import pygame
import cohere
import json, re
import buttons

pygame.init()

win = pygame.display.set_mode((680, 500))
pygame.display.set_caption("Mind Guardian 👼")

ST_ENEMY_IMG = pygame.image.load('enemy2.png')
ST_ENEMY_IMG = pygame.transform.scale(ST_ENEMY_IMG, (150, 150))
USER_IMG = pygame.image.load('user.png')
USER_IMG = pygame.transform.scale(USER_IMG, (80, 80))
BACKDROP = pygame.image.load('images/backdrop4.jpg')
BACKDROP = pygame.transform.scale(BACKDROP, (680, 500))
walkLeft = [pygame.image.load('trial/L1.png'), pygame.image.load('trial/L2.png'),pygame.image.load('trial/L3.png')]
walkRight = [pygame.image.load('trial/R1.png'), pygame.image.load('trial/R2.png'), pygame.image.load('trial/R3.png')]
walkLeft = [pygame.transform.scale(i, (80, 80)) for i in walkLeft]
walkRight = [pygame.transform.scale(i, (80, 80)) for i in walkRight]
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()


#button instances
start_button = buttons.Button(100,200,start_img,0.8)
exit_button = buttons.Button(450,200,exit_img,0.8)

clock = pygame.time.Clock()
# user_x = 0
# user_y = 550
# enemy_x = 550
# enemy_y = 150
# width = 40
# height = 60
# vel = 5
# isJump = False
# jumpCount = 10
# LEFT = False
# RIGHT = False
# walkCount = 0

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
        self.hitbox = (self.x + 5, self.y + 11, 75, 65)

    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 5, self.y + 11, 75, 65)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)


class shoot(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) 
        




def redrawScreen():  # Removed unused images parameter
    win.blit(BACKDROP, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    
    win.blit(text, (390, 10))
    man.draw(win)  # Changed to call draw on the instance
    q1.createBoxes(win)
    
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

class question(pygame.sprite.Sprite):
    def __init__(self, x, y, q_list):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.q_list = q_list
    
    def addRect(self, win, color, x, y):
        pygame.draw.rect(win, (color), (175, 75, x, y), 2)
    
    def addText(self, win, txt, color, x, y):
        win.blit(font.render(txt, True, (255, 0, 0)), (x, y))

    def createBoxes(self, win):
        self.createQues()
        self.addRect(win, (0, 0, 0), self.x, self.y)
        self.addText(win, self.q_list[0]["options"][0], (255, 0, 0), self.x+10, self.y+10)
        self.addRect(win, (0, 0, 0), self.x+50, self.y+50)
        self.addText(win, self.q_list[0]["options"][1], (255, 0, 0), self.x+60, self.y+60)
        self.addRect(win, (0, 0, 0), self.x+100, self.y+100)
        self.addText(win, self.q_list[0]["options"][2], (255, 0, 0), self.x+110, self.y+110)


        


    def createQues(self):
        co = cohere.Client('HXsbV5r53c0B94uaC6pcE60ScZhL37Ajr3nB1htX') # This is your trial API key
        response = co.generate(
        model='command',
        prompt="""Provide a list of 2 examples in form of Python dictionary of the most common negative thoughts about diversity, women empowerment, self-help, mental issues and underrepresented genders and 4 options for each thought out of which one might be the most correct option. Be sure to mention the correct answer with each thought. Complete the query in under 300 tokens, Only give me the complete python dictionary output do not give any text before the output or after the output.Sample example has been provided: {
            "thoughts": [
                {
                    "statement": "Diversity is a joke - it's just another word for less competent women, LGBTQ+, and non-white people taking the places of more competent white men.",
                    "options": [
                        "The world is a merit-based place",
                        "Embrace different perspectives and talents",        
                        "Hire people who look like you"
                    ],
                    "correct": "Embrace different perspectives and talents"  
                },
                {
                    "statement": "Women are too sensitive and they just need to get over the microaggressions they experience instead of being so vocal about them.",
                    "options": [
                        "Keep quiet or it will get worse",
                        "Recognize your privilege and speak up",
                        "Support and amplify their voices"
                    ],
                    "correct": "Support and amplify their voices"
                },
                {
                    "statement": "Mental health issues are a choice, and people just need to pull themselves up by their bootstraps and stop feeling sorry for themselves.",
                    "options": [
                        "Mental health is a choice",
                        "Seek professional help",
                        "Meditate and affirm your way out of depression and anxiety"
                    ],
                    "correct": "Seek professional help"
                },
                {
                    "statement": "Not enough people are talking about men's issues and the unique struggles they face, while everyone is too focused on women's issues.",
                    "options": [
                        "Focus on women's issues",
                        "Ignoring women's issues",
                        "Bridge the gap between women's and men's issues"    
                    ],
                    "correct": "Bridge the gap between women's and men's issues"
                }
            ]
        }""",
        max_tokens=500,
        temperature=0.1,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
        txt = response.generations[0].text
        print(txt)
        self.q_list = json.loads(txt.strip())["thoughts"]
    
    


class enemy(pygame.sprite.Sprite):
    enemy_walk_left = [pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]
    
    enemy_walk_right = [pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]

    def __init__(self, x, y, width, height, end):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 30, self.y + 25, 85, 110)
        self.health = 10
        self.visible = True
    
    def update(self):
        if not(self.visible):
            self.kill()
            print('Killed the daemon')


    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(ST_ENEMY_IMG, (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(ST_ENEMY_IMG, (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 30, self.y + 25, 85, 110)
        self.update()
        
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0]-self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                self.x += self.vel
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')



# LOOP
font = pygame.font.SysFont('comicsans', 20, True)
qlist = []
q1 = question(q_list=qlist, x=20, y=20)
man = player(200, 200, 64,64)
goblins = pygame.sprite.Group()
goblin = enemy(100, 150, 64, 64, 300)
goblins.add(goblin)
shootLoop = 0
score = 0
exit = False
bullets = []

while not exit:
    clock.tick(27)


# if start_button.draw(win):
#      print('START')
#   if exit_button.draw(win):
#       exit = True

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and goblin.visible == True:
                goblin.hit()
                score += 1 # NEW CODE
                bullets.pop(bullets.index(bullet))
        if bullet.x < 680 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(shoot(round(man.x + man.width // 2),round(man.y + man.height // 2), 6, (0,0,0), facing))
        
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 680 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = False
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawScreen()
    print('exit')

pygame.quit()