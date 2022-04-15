import pygame, sys, random, time 
 
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
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (400, 600) 
SPEED, USER_SPEED = 5, 5 
SCORE, COINS = 0, 0 
PAUSE, END = False, False 
 
#Setting up Fonts 
font = pygame.font.SysFont("Verdana", 60) 
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, BLACK) 
name = font.render("    Racer", True, BLACK) 
restart_button = font_small.render("click \"R\" to restart the game", True, BLACK) 
pause_button = font_small.render("click \"P\" to pause the game", True, BLACK)  
exit_button = font_small.render("click \"Q\" to exit the game", True, BLACK) 
 
#loading needed images 
background = pygame.image.load("street.png")  
enemy = pygame.image.load("Enemy.png") 
player = pygame.image.load("Player.png") 
 
#Create a green screen and show game splash screen 
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE) 
DISPLAYSURF.fill(GREEN) 
DISPLAYSURF.blit(name, (15, 150)) 
DISPLAYSURF.blit(restart_button, (30, 450)) 
DISPLAYSURF.blit(pause_button, (30, 500)) 
DISPLAYSURF.blit(exit_button, (30, 550)) 
pygame.display.set_caption("Racer") 
pygame.display.update() 
time.sleep(1) 
# monety
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30)) 
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, 360), -15) 
 
    def change_location(self): 
        self.rect.center = (random.randint(45, 360), -15) 
 
    def move(self): 
        self.rect.move_ip(0, 3) 
        if self.rect.top > 600: 
            self.rect.center = (random.randint(45, 360), -15)
 
    def draw(self): 
        DISPLAYSURF.blit(self.image, self.rect) 

class Coin1(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load('coin1.png'), (50,54)) 
        self.image = pygame.transform.scale(self.image, (30, 30)) 
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(45, 360), -1500) 
 
    def change_location(self): 
        self.rect.center = (random.randint(45, 360), -1500) 
 
    def move(self): 
        self.rect.move_ip(0, 3) 
        if self.rect.top > 600: 
            self.rect.center = (random.randint(30, 370), -1500)
 
    def draw(self): 
        DISPLAYSURF.blit(self.image, self.rect) 

# vrasheskaya car
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()  
        self.image = enemy 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -50) 
     
    def move(self): 
        global SCORE, USER_SPEED 
        self.rect.move_ip(0, SPEED) 
        if self.rect.top > 600: 
            SCORE += 1 
            if SCORE % 10 == 0 and SCORE != 0: 
                USER_SPEED += 1 
            self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), -50) 
    def draw(self): 
        DISPLAYSURF.blit(self.image, self.rect) 
# player
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()  
        self.image = player 
        self.rect = self.image.get_rect() 
        self.rect.center = (200, 520) 
    def move(self): 
        pressed_keys = pygame.key.get_pressed() 
        if self.rect.left > 5: 
            if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]: 
                self.rect.move_ip(-USER_SPEED, 0) 
        if self.rect.right < SCREEN_WIDTH - 5:         
            if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]: 
                self.rect.move_ip(USER_SPEED, 0) 
        # if self.rect.top > 5: 
        #     if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]: 
        #         self.rect.move_ip(0, -USER_SPEED) 
        # if self.rect.bottom < SCREEN_HEIGHT - 5:         
        #     if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]: 
        #         self.rect.move_ip(0, USER_SPEED) 
    def draw(self): 
        DISPLAYSURF.blit(self.image, self.rect)    
#Setting up Sprites         
P1 = Player() 
E1 = Enemy() 
C1 = Coin()
C2=Coin1()
#Creating Sprites Groups 
enemies = pygame.sprite.Group() 
enemies.add(E1) 
all_sprites = pygame.sprite.Group() 
all_sprites.add(P1) 
all_sprites.add(E1) 
all_sprites.add(C1) 
all_sprites.add(C2)
coins = pygame.sprite.Group() 
coins.add(C1) 
coins1 = pygame.sprite.Group()
coins1.add(C2)
#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1 
pygame.time.set_timer(INC_SPEED, 2500) 
#Starting point of our game time 
start_time = time.time() 
background_music = pygame.mixer.music.load("background.wav") 
pygame.mixer.music.play(-1) 
#Game Loop 
while True: 
    #Cycles through all events occuring   
    for event in pygame.event.get(): 
        if event.type == INC_SPEED: 
            SPEED += 0.5       
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q): 
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p: 
            if PAUSE: PAUSE = False 
            else: PAUSE = True      
        #Restart the game and initialize main variables 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r: 
            for entity in all_sprites: 
                entity.__init__()  
            C1.change_location() 
            SCORE, COINS = 0, 0 
            SPEED, USER_SPEED = 5, 5 
            PAUSE, END = False, False 
            start_time = time.time() 
            background_music = pygame.mixer.music.load("background.wav") 
            pygame.mixer.music.play(-1) 
    #Check game state      
    if END: 
        pass 
    else:     
        #Check game state 
        if PAUSE: 
            pass 
        else: 
            DISPLAYSURF.blit(background, (0, 0)) 
            scores = font_small.render(str(SCORE), True, BLACK) 
            coin_scores = font_small.render(str(COINS), True, BLACK) 
            current_speed = font_small.render("Your speed: " + str(USER_SPEED), True, BLACK) 
            enemy_speed = font_small.render("Enemy speed: " + str(SPEED), True, BLACK) 
            DISPLAYSURF.blit(scores, (10, 10)) 
            DISPLAYSURF.blit(coin_scores, (365, 10)) 
            DISPLAYSURF.blit(current_speed, (10, 50)) 
            DISPLAYSURF.blit(enemy_speed, (10, 90)) 
           
            #Moves and Re-draws all Sprites 
            for entity in all_sprites: 
                entity.move() 
                entity.draw() 
           
            #Checks collision and change coordinates of the coin randomly    
            if pygame.sprite.spritecollideany(P1, coins): 
                COINS += 1 
                pygame.mixer.Sound('crash.mp3').play() 
                C1.change_location() 
            elif pygame.sprite.spritecollideany(P1, coins1): 
                COINS += 3 
                pygame.mixer.Sound('crash.mp3').play() 
                C2.change_location() 
           
            #To set end point 
            end_time = time.time() 
            cnt = round(end_time - start_time, 2) 
            game_time = font_small.render("time: " + str(cnt), True, BLACK)
            DISPLAYSURF.blit(game_time, (10, 140)) 
            
            #To be run if collision occurs between Player and Enemy 
            if pygame.sprite.spritecollideany(P1, enemies):      
                END = True 
                pygame.mixer.music.stop() 
                pygame.mixer.Sound('crash.wav').play() 
                time.sleep(1) 
 
                scores = font_small.render("Your Score: " + str(SCORE), True, BLACK) # how much car ty proshel
                coin_scores = font_small.render("Your Coins: " + str(COINS), True, BLACK) # sum vseh monet po vessam
                game_time = font_small.render("Seconds: " + str(cnt), True, BLACK) # scolko sec provel v vnuti igry
 
                DISPLAYSURF.fill(WHITE) 
                DISPLAYSURF.blit(game_over, (30, 150)) 
                DISPLAYSURF.blit(game_time, (30, 300)) 
                DISPLAYSURF.blit(scores, (30, 350)) 
                DISPLAYSURF.blit(coin_scores, (30, 400)) 
                DISPLAYSURF.blit(restart_button, (30, 450)) 
                DISPLAYSURF.blit(pause_button, (30, 500)) 
                DISPLAYSURF.blit(exit_button, (30, 550)) 
                 
                pygame.display.update() 
                    
            pygame.display.update() 
            FramePerSec.tick(FPS)