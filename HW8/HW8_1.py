#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
MONEY = 0                 # Adding money variable (Lab 8)
CURRENT_CURRENCY = random.randint(0, 2)      # Adding coin type variable (Lab 9)

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("C:\\Users\\Aldiy\\work\\HW8\\HW8_files\\AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\Aldiy\\work\\HW8\\HW8_files\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED + MONEY // 2) #Adding money's affection on speed (Lab 9)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\Aldiy\\work\\HW8\\HW8_files\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Tiin(pygame.sprite.Sprite):  # Adding coins, same "Ai" as enemies (Lab 8)
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\Aldiy\\work\\HW8\\HW8_files\\Tiin.png")
        self.image = pygame.transform.scale(self.image, (40, 30)) #Scaling image (Lab 8)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
    
    def randomize(self):     #Adding randomizing function (Lab 9)
        global CURRENT_CURRENCY
        CURRENT_CURRENCY = random.randint(0, 2)
        if CURRENT_CURRENCY == 0:
            self.image = pygame.transform.scale(self.image, (20, 15))
        if CURRENT_CURRENCY == 1:
            self.image = pygame.transform.scale(self.image, (40, 30))
        if CURRENT_CURRENCY == 2:
            self.image = pygame.transform.scale(self.image, (60, 45))

    def move(self):
        self.rect.move_ip(0, 10)  #Changed speed to add difference from enemies (Lab 8)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.randomize() #Randomizing the coin after it dissapears (Lab 9)
    
    def collected(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Tiin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  #Adding coins into the mix (Lab 8)
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {str(SCORE)}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    money_count = font_small.render(f"Money: {str(MONEY)}", True, BLACK) #Adding money text
    DISPLAYSURF.blit(money_count, (10,30))        #And showing it                   (Lab 8)

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, coins):
        MONEY += 3 - CURRENT_CURRENCY
        C1.collected()                  #Making money dissapear when collected (Lab 8)
        C1.randomize()                  #Randomizing the coin type after collection (Lab 9)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:\\Users\\Aldiy\\work\\HW8\\HW8_files\\crash.wav').play()
        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
                entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()