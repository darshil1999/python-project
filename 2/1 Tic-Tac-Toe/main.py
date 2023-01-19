import pygame as pg, sys
from pygame.locals import *
import time

xo = 'x'
winner = None
draw = False
width=400
height=400
white = (255,255,255)
line_color = (10,10,10)

ttt = [[None]*3,[None]*3,[None]*3]

pg.init()
fps = 30
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

x_img = pg.transform.scale(x_img,(80,80))
o_img = pg.transform.scale(o_img,(80,80))

def game_opening():
    time.sleep(1)
    screen.fill(white)

    # vertical lines
    pg.draw.line(screen, line_color, (width/3,0), (width/3, height),7)
    pg.draw.line(screen, line_color, (width/3*2,0), (width/3*2, height),7)

    # horizontal lines
    pg.draw.line(screen, line_color, (0,height/3), (width, height/3),7)
    pg.draw.line(screen, line_color, (0,height/3*2), (width, height/3*2),7)

    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = xo.upper() + "'s Turn"
    else:
        message = winner.upper() + "Won!"
    if draw:
        message = "Game Draw!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255,255,255))

    screen.fill((0,0,0,),(0,400,500,100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global ttt, winner, draw

    for row in range(0,3):
        if ((ttt[row][0] == ttt[row][1] == ttt[row][2]) and (ttt[row][0] is not None)):
            winner = ttt[row][0]
            pg.draw.line(screen,(255,0,0), ((row+1)*height/3 - height/6),)
            break

    for col in range(0,3):
        if (ttt[0][col] == ttt[1][col] == ttt[2][col] and (ttt[0][col] is not None)):
            winner = ttt[0][col]
            pg.draw.line(screen, (255,0,0), ((col + 1)* width/3 - width/6, 0), ((col + 1)* width/3 - width/6, height),4)
            break

    if (ttt[0][0] == ttt[1][1] == ttt[2][2]) and (ttt[0][0] is not None):
        winner = ttt[0][0]
        pg.draw.line(screen, (255,70,70), (50,50), (350,350), 4)

    if (ttt[0][2] == ttt[1][1] == ttt[2][0]) and (ttt[0][0] is not None):
        winner = ttt[0][2]
        pg.draw.line(screen, (255,70,70), (50,50), (350,350), 4)

    if (all([all(row) for row in ttt]) and winner is not None):
        draw = True
    
    draw_status()

def draw_xo(row,col):
    global ttt, xo
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 +30
    if row == 3:
        posx = width/3*2 +30
        
    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 +30
    if col == 3:
        posy = height/3*2 +30

    ttt[row-1][col-1] = xo
    if (xo == 'x'):
        screen.blit(x_img, (posy, posx))
        xo = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        xo = 'x'
    pg.display.update()

def userclick():
    x,y = pg.mouse.get_pos()

    if (x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif (x<width):
        col = 3
    else:
        col = None

    if (y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif (y<height):
        row = 3
    else:
        row = None

    if (row and col and ttt[row - 1][col - 1] is None):
        global xo

        draw_xo(row,col)
        check_win()

def reset():
    global ttt, xo, winner, draw

    time.sleep(3)
    xo = 'x'
    draw = False
    game_opening()
    winner = None
    ttt = [[None]*3, [None]*3, [None]*3]

game_opening()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            userclick()
            if (winner or draw):
                reset()

    pg.display.update()
    clock.tick(fps)