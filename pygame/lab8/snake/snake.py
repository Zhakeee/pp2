import pygame
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

pygame.init()
screen = pygame.display.set_mode([width, height]) # background
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True) 
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level=pygame.font.SysFont('Arial', 26, bold=True)



while True:
    screen.fill(pygame.Color('pink'))

    # drawing snake, apple, walls
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    for i, j in walls:
        pygame.draw.rect(screen, pygame.Color('black'), (i, j, block - 1, block - 1))


    # show score
    render_score = font_score.render(f'Score: {score}', True, pygame.Color('black'))
    render_level = font_level.render(f'Level: {cnt}', True, pygame.Color('black'))


    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if not(x < 0 or x > width - block or y < 0 or y > height - block or len(snake) > len(set(snake)) or snake in walls):
        screen.blit(render_score, (5, 5))    
        screen.blit(render_level, (5, 35))
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

    # eating apple
    if snake[-1] == apple:
        while apple in snake or apple in walls:
            apple = randrange(0, width, block), randrange(0, height, block)
        length += 1
        score += 1
        if not score % 4:
            fps += 1
            cnt+=1

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    # control
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