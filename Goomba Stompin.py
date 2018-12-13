import pygame
pygame.init()

win = pygame.display.set_mode((550, 500))#size of window

pygame.display.set_caption ("Sick Vydia Game")#sets name of window


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
backgroundfile = pygame.image.load('bg.png')
char = pygame.image.load('idle.png')

clock = pygame.time.Clock()
#player class
class player(object):
        def __init__(self, x, y, width, height,):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.vel = 5
                self.isJump = False
                self.jumpCount = 10
                self.left = False
                self.right = False
                self.walkCount = 0
                self.standing = True
                self.hitbox = (self.x + 17, self.y + 11, 29,52)

        def draw(self,win):
                if self.walkCount + 1 >= 27:
                        self.walkCount = 0
                if self.left:
                        win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                        self.walkCount += 1
                elif self.right:
                        win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                        self.walkCount += 1
                else:
                        win.blit(char, (self.x, self.y))
                self.hitbox = (self.x, self.y, 17,30)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)


#enemy
class enemy(object):
        walkRight = [pygame.image.load('ER1.png'), pygame.image.load('ER2.png'), pygame.image.load('ER3.png'), pygame.image.load('ER4.png'), pygame.image.load('ER5.png'), pygame.image.load('ER6.png')] 
        walkLeft = [pygame.image.load('EL1.png'), pygame.image.load('EL2.png'), pygame.image.load('EL3.png'), pygame.image.load('EL4.png'), pygame.image.load('EL5.png'),pygame.image.load('EL6.png')]
        def __init__(self, x, y, width, height, end):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [self.x, self.end]
                self.walkCount = 0
                self.vel = 3
                self.hitbox = (self.x, self.y, 25, 17)
        
        def draw(self,win):
                self.move()
                if self.walkCount + 1 >= 33:
                        self.walkCount = 0

                if self.vel > 0:
                        win.blit(self.walkRight[self.walkCount //6], (self.x, self.y))
                        self.walkCount += 1
                else:
                        win.blit(self.walkLeft[self.walkCount //6], (self.x, self.y))
                        self.walkCount += 1
                self.hitbox = (self.x - 3, self.y, 25, 17)
                pygame.draw.rect(win, (255,0,0), self.hitbox ,2)
                
                

        def move(self):
                if self.vel > 0:
                    if self.x + self.vel < self.path[1]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
                else:
                    if self.x - self.vel > self.path[0]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
                              
        def hit(self):
                print('hit')
                pass
        

       

def redrawGameWindow():
        win.blit(backgroundfile, (0,0))
        man.draw(win)
        goomba.draw(win)
        pygame.display.update()

#Core loop

man = player(400, 410, 64, 64)
goomba = enemy(100, 424, 64, 64, 450)
run = True
while run:
        clock.tick (27)

        for event in pygame.event.get():#checks for inputs (mouse movement, keyboard press, etc.
            if event.type == pygame.QUIT:#allows x in corner to quit game
                run = False
        #sets key inputs to move character and prevents them from running off, and the formula for jumping
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and man.x > man.vel:                           
               man.x -= man.vel
               man.left = True
               man.right = False
        elif keys[pygame.K_RIGHT] and man.x < 600 - man.width - man.vel:
                man.x += man.vel
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
                        neg = 1
                        if man.jumpCount < 0:
                                neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.2 * neg
                        man.jumpCount -= 1
                else:
                        man.isJump = False
                        man.jumpCount = 10

        redrawGameWindow()

pygame.quit()
