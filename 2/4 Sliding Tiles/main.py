# import libraries
import pygame
import sys, os, random

# initialize window
width = 800
height = 600
fps = 12
pygame.init()
pygame.display.set_caption('Sliding Tiles')
gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
brown = (100,40,0)

background = pygame.image.load('white.png') # setting game background image
background = pygame.transform.scale(background,(800, 600))

font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 70)

# class for whole game
class Generate_puzzle:
    def __init__(self, gridsize, tilesize, margin):
        self.gridsize, self.tilesize, self.margin = gridsize, tilesize, margin

        self.tiles_no = gridsize[0]*gridsize[1] - 1 # no of tiles
        self.tiles = [(x,y) for y in range(gridsize[1]) for x in range(gridsize[0])] # coordinate of tiles
        self.tilepos = {(x,y):(x*(tilesize + margin) + margin, y * (tilesize + margin) + margin) for y in range(gridsize[1]) for x in range(gridsize[0])}
        self.prev = None

        self.tile_images = []
        font = pygame.font.Font(None, 80)

        for i in range(self.tiles_no):
            image = pygame.Surface((tilesize, tilesize)) # display tiles
            image.fill(brown)
            text = font.render(str(i + 1), 2, (255,255,255)) # text on tiles
            width, height = text.get_size() # text size on tiles
            image.blit(text, ((tilesize-width)/2, (tilesize-height)/2))
            # display text in the middle of the tile
            self.tile_images += [image]

    def blank_pos(self):
        return self.tiles[-1]

    def set_blank_pos(self,pos):
        self.tiles[-1] = pos
    opentile = property(blank_pos, set_blank_pos) # get and set the pos of blank

    def swith_tile(self, tile):
        self.tiles[self.tiles.index(tile)] = self.opentile
        self.opentile = tile
        self.prev = self.opentile

    def check_in_grid(self, tile):
        return tile[0] >= 0 and tile[0] < self.gridsize[0] and tile[1] >= 0 and tile[1] < self.gridsize[1]

    # adjacent tile position to blank (which tiles cna move to blank position)
    def close_to(self): 
        x,y = self.opentile
        return (x-1,y),(x+1,y),(x,y-1),(x,y+1)

    def set_tile_randomly(self):
        adj = self.close_to()
        adj = [pos for pos in adj if self.check_in_grid(pos) and pos != self.prev]
        tile = random.choice(adj)
        self.swith_tile(tile)

    # update tile position
    def update_tile_pos(self, dt):
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

        if mouse[0]:
            x,y = mpos[0] % (self.tilesize + self.margin), mpos[1] % (self.tilesize + self.margin)
            if x > self.margin and y > self.margin:
                tile = mpos[0] // self.tilesize, mpos[1] // self.tilesize
                if self.check_in_grid(tile) and tile in self.close_to():
                    self.swith_tile(tile)

    #  draw tiles in particular positioned
    def draw_tile(self, gameDisplay):
        for i in range(self.tiles_no):
            x,y = self.tilepos[self.tiles[i]]
            gameDisplay.blit(self.tile_images[i], (x,y))

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(100):
                    self.set_tile_randomly()


# Levels of game
def level_screen():
    l1, l1_rect = makeText('Level 1', red, True, 100, 40)
    l2, l2_rect = makeText('Level 2', red, True, 500, 40)
    l3, l3_rect = makeText('Level 3', red, True, 100, 180)
    l4, l4_rect = makeText('Level 4', red, True, 500, 180)
    l5, l5_rect = makeText('Level 5', red, True, 100, 320)
    l6, l6_rect = makeText('Level 6', red, True, 500, 320)
    l7, l7_rect = makeText('Level 7', red, True, 100, 460)
    l8, l8_rect = makeText('Level 8', red, True, 500, 460)

    gameDisplay.blit(l1, l1_rect)
    gameDisplay.blit(l2, l2_rect)
    gameDisplay.blit(l3, l3_rect)
    gameDisplay.blit(l4, l4_rect)
    gameDisplay.blit(l5, l5_rect)
    gameDisplay.blit(l6, l6_rect)
    gameDisplay.blit(l7, l7_rect)
    gameDisplay.blit(l8, l8_rect)

    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if l1_rect.collidepoint(mpos):
            level1()
        elif l2_rect.collidepoint(mpos):
            level2()
        elif l3_rect.collidepoint(mpos):
            level3()
        elif l4_rect.collidepoint(mpos):
            level4()
        elif l5_rect.collidepoint(mpos):
            level5()
        elif l6_rect.collidepoint(mpos):
            level6()
        elif l7_rect.collidepoint(mpos):
            level7()
        elif l8_rect.collidepoint(mpos):
            level8()

def level1():
    program = Generate_puzzle((3,3),80,5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay, 'PRESS SAPCE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level2():
    program = Generate_puzzle((3,4), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level3():
    program = Generate_puzzle((4,3), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level4():
    program = Generate_puzzle((4,4), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level5():
    program = Generate_puzzle((4,5), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level6():
    program = Generate_puzzle((5,5), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level7():
    program = Generate_puzzle((5,4), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level8():
    program = Generate_puzzle((6,5), 80, 5)
    while True:
        dt = clock.tick() / 1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60, 370, 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

# create the Surface and Rect objects for some text.
def makeText(text, color, bgcolor, top, left):
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)    


# Generic method to draw fonts on the screen   
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, brown)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

##front screen of the game

def game_front_screen():
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "SLIDING TILE GAME!", 90, width / 2, height / 4)
    draw_text(gameDisplay, "Press a key to begin!", 80, width / 2, height * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                

# mainloop

game_over = True        
game_running = True 
while game_running :
    if game_over :
        game_front_screen()           #front screen of the game
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:          
            game_running = False
    gameDisplay.blit(background, (0,0))  
    level_screen()                ##goes to second screen of the game which is levels 

    pygame.display.update()
    clock.tick(fps)
pygame.quit()