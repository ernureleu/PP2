import pygame, random
# ЦВЕТА
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
# РОМБ 
def Rhombus(screen, color, x, y, X1, Y1, radius):
    x1 = x
    x2 = X1
    y1 = y
    y2 = Y1
    line1 = (x1,(y1+y2)/2)
    line2 = ((x1+x2)/2,y1)
    line3 = (x2,(y1+y2)/2)
    line4 = ((x1+x2)/2,y2)
    pygame.draw.polygon(screen, pygame.Color(color), (line1,line2,line3, line4),radius)


def RightTriangle(screen,color, x, y, X1, Y1, radius,):
    x1 = x
    x2 = X1
    y1 = y
    y2 = Y1
    z1 = x1
    z2 = y2
    pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1),(x2,y2),(z1,z2)),radius)

def Square(screen, color, x, y, X1, Y1, radius):
    x1 = x
    x2 = X1
    y1 = y
    y2 = Y1
    line1 = abs(x2-x1)
    line2 = abs(y2-y1)
    squaree = min(line1,line2)
    pygame.draw.rect(screen, pygame.Color(color), (x1,y2,squaree,squaree), radius)




def EquilateralTriangle(surface,color, x, y, X1, Y1, radius):
    x1 = x
    x2 = X1
    y1 = y
    y2 = Y1
    z1 = (abs(x1)+abs(x2))/2
    heigh = (3**0.5) * (abs(x2-x1))/2
    if y2 > y1:
        pygame.draw.polygon(surface, pygame.Color(color), ((x1,y1),(x2,y2),(z1,y2 - heigh)),radius)
    else:
        pygame.draw.polygon(surface, pygame.Color(color), ((x1,y1),(x2,y2),(z1,y1-heigh)),radius)

# ПРЯМОУОЛНИК
def Rectangle(surface, color, x, y, x1, y1, size):
    pygame.draw.rect(surface, color, [x, y, abs(x1 - x), abs(y - y1)], size)
#КРУГ
def Circle(screen, color, x, y, X1, Y1, width):
    x1 = x
    x2 = X1
    y1 = y
    y2 = Y1
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


#ЛИНИЯ
def Line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    coor1 = y2 - y1
    coor2 = x1 - x2
    coor3 = x2 * y1 - x1 * y2
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-coor3 - coor1 * x) / coor2
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-coor3 - coor2 * y) / coor1
            pygame.draw.circle(screen, color, (x, y), width)


main_pressed = False
main_rect = True
background = pygame.image.load("white.png")


def main(background):
    white_bg = pygame.image.load("white.png")
    screen = pygame.display.set_mode((800, 600))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    main_rect = True
    main_circle = True
    main_save = False
    main_clear = False
    main_load = False
    main_triangle = True
    main_phombus = True
    main_righttriangle = True
    main_square = True
    tool = 'kist'
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'black': (0, 0, 0),
        'eraser': (255, 255, 255)
    }
    screen.blit(background, (0, 0))
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    pass
                if event.key == pygame.K_F4 and alt_held:
                    pass
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_DOWN:
                    radius -= 1
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key ==pygame.K_1:
                    tool = 'kist'
                if event.key ==pygame.K_2:
                    tool = 'rectangle'
                if event.key ==pygame.K_3:
                    tool = 'circle'
                if event.key == pygame.K_4:
                    tool = 'triangle'
                if event.key == pygame.K_5:
                    tool = 'righttriangle'
                if event.key == pygame.K_6:
                    tool = 'phombus'
                if event.key == pygame.K_7:
                    tool = 'square'
                if event.key ==pygame.K_e:
                    mode = 'eraser'
                if event.key ==pygame.K_z:
                    main_save = True
                if event.key ==pygame.K_x:
                    main_load = True
                if event.key ==pygame.K_c:
                    main_clear = True
                if event.key ==pygame.K_q:
                    mode = 'random'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_rect:
                    prev_pos = pygame.mouse.get_pos()
                    main_rect = False
                if main_circle:
                    prev_pos = pygame.mouse.get_pos()
                    main_circle = False
                if main_triangle:
                    prev_pos = pygame.mouse.get_pos()
                    main_triangle = False
                if main_phombus:
                    prev_pos = pygame.mouse.get_pos()
                    main_phombus = True
                if main_righttriangle:
                    prev_pos = pygame.mouse.get_pos()
                    main_righttriangle = False
                if main_square:
                    prev_pos = pygame.mouse.get_pos()
                    main_square = False
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                if tool == 'kist':
                    pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
                
            if event.type == pygame.MOUSEBUTTONUP:
                COORX = pygame.mouse.get_pos()
                if tool == 'rectangle':
                    Rectangle(screen, color, prev_pos[0], prev_pos[1], COORX[0], COORX[1], radius)
                    main_rect = True
                if tool == 'triangle':
                    EquilateralTriangle(screen,color, prev_pos[0], prev_pos[1],COORX[0], COORX[1] ,radius)
                if tool == 'phombus':
                    Rhombus(screen,color, prev_pos[0], prev_pos[1], COORX[0], COORX[1], radius)
                if tool == 'righttriangle':
                    RightTriangle(screen,color, prev_pos[0], prev_pos[1], COORX[0], COORX[1], radius)
                if tool == 'circle':
                    Circle(screen, color, prev_pos[0], prev_pos[1], COORX[0], COORX[1], radius)
                    main_circle = True
                if tool == 'square':
                    Square(screen, color, prev_pos[0], prev_pos[1], COORX[0], COORX[1], radius)
                    main_square = True
                
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on and (tool != 'rectangle' and tool != 'circle' and tool != 'triangle' and tool != 'righttriangle' and tool != 'phombus' and tool != 'square'):
                    Line(screen, last_pos, event.pos, radius, color)
                last_pos = event.pos
        if main_save:
            pygame.image.save(screen, 'save.png')
            main_save = False
        if main_clear:
            break
        if main_load:
            save_background = pygame.image.load('save.png')
            break

        pygame.display.flip()

    if main_clear:
        main(white_bg)
    if main_load:
        main(save_background)
    pygame.quit()


main(background)