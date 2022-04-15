import pygame 
 
number_of_error = 1 
 
# function for if ball выйдет из границ 
def if_error(): 
    global number_of_error 
    number_of_error += 1 
 
 
pygame.init() 
SIZE = (400, 400) 
FPS = 60 
step = 20 
r = 25 
x, y = 30, 30 
 
screen = pygame.display.set_mode(SIZE) 
 
clock = pygame.time.Clock() 
screen.fill(pygame.Color(255,255,255)) 
 
while True: 
    # QUIT 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit() 
 
    # buttons 
        if event.type == pygame.KEYDOWN: 
            pressed = pygame.key.get_pressed() 
            if pressed[pygame.K_DOWN]: 
                if y+step+r <= SIZE[1]: 
                    y += step 
                else: 
                    if_error() 
            elif pressed[pygame.K_UP]: 
                if y-step-r >= 0: 
                    y -= step 
                else: 
                    if_error() 
            elif pressed[pygame.K_LEFT]: 
                if x-step-r >= 0: 
                    x -= step 
                else: 
                    if_error() 
            elif pressed[pygame.K_RIGHT]: 
                if x+step+r <= SIZE[0]: 
                    x += step 
                else: 
                    if_error() 
 
 
    screen.fill(pygame.Color(255,255,255)) 
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), (x, y), r) 
 
    pygame.display.flip() 
    clock.tick(FPS)