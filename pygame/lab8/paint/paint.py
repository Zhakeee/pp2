import pygame, time

WIDTH, HEIGHT = 1200, 800
FPS = 60 
draw=False # нажатие, зажатие - рисуем, отжали - не рисуем 
last_pos=(0,0)
radius=15
dic="1-yellow 2-green 3-black 4-red 5-grey 6-pink 7-purple 8-orange 9-brown"
md="circle-c rectangle-r pen-p erase-/"
color=(0, 0, 0)
mode='pen' # автоматов мышка будет ричовать в этом режиме

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint") # paint's name
clock=pygame.time.Clock()
screen.fill(pygame.Color('white')) # background color
font_r=pygame.font.SysFont('Arial', 26, bold=True) # шрифт и стиль числа в левым вверхнем углу
font_color=pygame.font.SysFont('Arial', 24)
font_md=pygame.font.SysFont('Arial', 24)



# функция для использования режима рисования
def drawline(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x)/B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else: 
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = ( -C - B*y)/A
            pygame.draw.circle(screen, pygame.Color(color),(x, y), width)
# режим использования круга
def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x=(x1+x2)/2
    y=(y1+y2)/2
    radius = abs(x1-x2)/2
    pygame.draw.circle(screen, pygame.Color(color),(x,y),radius, width)
# режим для использования прямоугольника
def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr=abs(x1-x2)
    height=abs(y1-y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

screen.fill(pygame.Color('White'))
while True:
    # выход из игры
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        # режимы и цвета для использования круга и прямоугольник, также для того чтобы поменять цвет
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_r:
                mode ='rectangle'
            if event.key == pygame.K_c:
                mode ='circle'
            if event.key==pygame.K_p:
                mode='pen'
            if event.key==pygame.K_SLASH:
                mode='remove'
            if event.key==pygame.K_q: # clear screen
                screen.fill('white')
            if event.key==pygame.K_1:
                color='yellow'
            if event.key==pygame.K_2:
                color='green'
            if event.key==pygame.K_3:
                color='black'
            if event.key==pygame.K_4:
                color='red'
            if event.key==pygame.K_5:
                color='grey'
            if event.key==pygame.K_6:
                color='pink'
            if event.key==pygame.K_7:
                color='purple'
            if event.key==pygame.K_8:
                color='orange'
            if event.key==pygame.K_9:
                color='brown'
                
            # кнопки вверх и вниз меняют размер шрифта которым рисуем
            if event.key==pygame.K_UP:
                radius=min(100, radius+1)
            if event.key==pygame.K_DOWN:
                radius=max(1, radius-1)
        
        if event.type== pygame.MOUSEBUTTONDOWN: # нажатие мышки
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos=event.pos
        if event.type == pygame.MOUSEBUTTONUP: # отпускание мышки
            if mode=='rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode =='circle':
                drawCircle(screen,prevPos, event.pos,radius, color)
            draw=False
        if event.type == pygame.MOUSEMOTION: # перемещение мышки
            if draw==True and mode == 'pen':
                drawline(screen, last_pos, event.pos, radius, color)
            elif draw and mode=='remove':
                drawline(screen,last_pos, event.pos, radius, 'White')
            last_pos=event.pos

    # show radius and color
    pygame.draw.rect(screen, pygame.Color('white'), (5,5,50,50))
    pygame.draw.rect(screen, pygame.Color('white'), (5,25,630,50))
    render_r=font_r.render(f'{radius}' , True ,pygame.Color(color))
    render_color=font_color.render(f'{dic}' , True ,pygame.Color('black'))
    render_md=font_md.render(f'{md}' , True ,pygame.Color('black'))
    screen.blit(render_r, (5,5))
    screen.blit(render_color, (5,25))
    screen.blit(render_md, (5, 45))

    pygame.display.flip()
    clock.tick(FPS)