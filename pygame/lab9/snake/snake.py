import pygame,time
from random import randrange


size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block)
apple = randrange(0, width, block), randrange(0, height, block)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
score = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 9
cnt=1
walls = []
food_timer=0
running=True
start_time=0
time_limit=5
extra_apple=False
run=False

pygame.init()
screen = pygame.display.set_mode([width, height]) # background
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True) 
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level=pygame.font.SysFont('Arial', 26, bold=True)
next_level=font_level.render("Next level", True, pygame.Color('black'))
levels = {1 : 6, 2 : 15, 3 : 20, 4 : 25, 5 : 50} # key - current level, value - apples to eat

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(pygame.Color('pink'))

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
    # show score
    render_score = font_score.render(f'Score: {score}', True, pygame.Color('black'))
    render_level = font_level.render(f'Level: {cnt}', True, pygame.Color('black'))
    timer = font_score.render(f"time: {str(int(6 + start_time - time.time()))}", True, (255, 255, 255))

    # drawing snake, apple, walls
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    for i, j in walls:
        pygame.draw.rect(screen, pygame.Color('black'), (i, j, block - 1, block - 1))
    
    if food_timer==3:
        extra_apple=True
        if not run:
            start_time=time.time()
            run=True
        if time.time()-start_time<=time_limit:
            pygame.draw.rect(screen, pygame.Color('yellow'), (*apple, block, block))
            screen.blit(timer, (50, 10))
        else:
            run=False
            extra_apple=False
            food_timer=0
    else:
        pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))




    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if not(x < 0 or x > width - block or y < 0 or y > height - block or len(snake) > len(set(snake)) or snake in walls):
        screen.blit(render_score, (5, 5))    
        screen.blit(render_level, (5, 35))
        # screen.blit(timer, (20, 5))
    else:
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('black'))
            screen.blit(render_end, (335, 100))
            screen.blit(render_score, (350, 170))
            screen.blit(render_level, (350, 200))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    #next level
    if length >= levels[cnt]:


        cnt += 1
        fps += 0.5


    # eating apple
    if snake[-1] == apple:
        while apple in snake or apple in walls or timer==0:
            apple = randrange(0, width, block), randrange(0, height, block)
        if extra_apple:
            score += 3
            food_timer=0
            length += 1
            extra_apple=False
        else:
            food_timer+=1
            score+=1
            length+=1
        

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(fps)