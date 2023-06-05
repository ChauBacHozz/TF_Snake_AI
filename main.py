import pygame as pg
import random
import math
pg.init()

back = (0, 0, 0)
DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 600
nrows = 20
ncols = 20 
grid_val = DISPLAY_HEIGHT / nrows
score = 0
gameDisplay = pg.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pg.display.set_caption('Snake')
gameDisplay.fill(back)
running = True
losed = False
clock = pg.time.Clock()
start_ticks = pg.time.get_ticks()

fontSize = 64
font = pg.font.SysFont(name = 'freesansbold',size = fontSize)




def draw_arrow(screen, colour, start, end, thickness):
    pg.draw.line(screen,colour,start,end, thickness)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pg.draw.polygon(screen, colour, ((end[0]+20*math.sin(math.radians(rotation)), end[1]+20*math.cos(math.radians(rotation))), (end[0]+20*math.sin(math.radians(rotation-120)), end[1]+20*math.cos(math.radians(rotation-120))), (end[0]+20*math.sin(math.radians(rotation+120)), end[1]+20*math.cos(math.radians(rotation+120)))))

def drawDirection(screen, colour, pos, width, active_arrows = [0, 0, 0, 0], active_colour = (255, 0, 0)):
    # Trên dưới trái phải
    for i in (-1, 1):
        if active_arrows[i + 1] == 1:
            draw_arrow(screen, active_colour, (pos[0], i * 20 + pos[1]), (pos[0], i * (width + 20) + pos[1]), 20)
        else:
            draw_arrow(screen, colour, (pos[0], i * 20 + pos[1]), (pos[0], i * (width + 20) + pos[1]), 20)
    
    for i in (-1, 1):
        if active_arrows[i + 2] == 1:
            draw_arrow(screen, active_colour, (i * 20 + pos[0], pos[1]), (i * (width + 20) + pos[0], pos[1]), 20)
        else:
            draw_arrow(screen, colour, (i * 20 + pos[0], pos[1]), (i * (width + 20) + pos[0], pos[1]), 20)

def draw_text(text,x,y,color):
    label = font.render(text, True, color)
    gameDisplay.blit(label, (x,y))

def drawGrid():
    for i in range(nrows + 1):
        pg.draw.line(gameDisplay, (255, 255, 255),
                     (0, i * grid_val), (DISPLAY_HEIGHT, i * grid_val))
    for i in range(ncols + 1):
        pg.draw.line(gameDisplay, (255, 255, 255),
                     (i * grid_val, 0), (i * grid_val, DISPLAY_HEIGHT))
class Node():
    def __init__(self, color):
        self.color = color
        self.xpos = -1
        self.ypos = -1
    def draw(self):
        pg.draw.rect(gameDisplay ,rect = pg.Rect(self.xpos,
                                                  self.ypos, grid_val, grid_val), color=self.color)

class Snake():
    def __init__(self) -> None:
        self.body = [Node((0,180,0))]
        self.direction = "R"
        self.width = grid_val
    def spawn(self):
        self.body[0].xpos = 4 * grid_val
        self.body[0].ypos = 10 * grid_val
        self.body.append(Node((0, 255, 0)))
    def draw(self):
        for node in self.body:
            node.draw()
    def move(self):
        for i in reversed (range(1, len(self.body))):
            self.body[i].xpos = self.body[i - 1].xpos
            self.body[i].ypos = self.body[i - 1].ypos
        if self.direction == "U":
            self.body[0].ypos -= self.width
        if self.direction == "D":
            self.body[0].ypos += self.width
        if self.direction == "L":
            self.body[0].xpos -= self.width
        if self.direction == "R":
            self.body[0].xpos += self.width

    def turn(self, type):
        if type == "U" and self.direction != "D":
            self.direction = "U"
        if type == "D" and self.direction != "U":
            self.direction = "D"
        if type == "L" and self.direction != "R":
            self.direction = "L"
        if type == "R" and self.direction != "L":
            self.direction = "R"
    def checkApplecollision(self, apple_xpos, apple_ypos):
        global score
        if (self.body[0].xpos == apple_xpos and self.body[0].ypos == apple_ypos):
            score += 1
            self.body.append(Node((0, 255, 0)))
            return True
    def checkWallcollision(self):
        if (self.body[0].xpos < -10 or self.body[0].xpos > DISPLAY_HEIGHT - self.width
            or self.body[0].ypos < -10 or self.body[0].ypos > DISPLAY_HEIGHT - self.width):
            return True
        for node in self.body[1:]:
            if node.xpos == self.body[0].xpos and node.ypos == self.body[0].ypos:
                return True
        return False
    

class Apple():
    def __init__(self) -> None:
        self.color = (255, 0, 0)
        self.width = grid_val
    def spawn_first(self):
        self.xpos = random.randint(0, 19) * self.width
        self.ypos = random.randint(0, 19) * self.width
    def spawn_aftereaten(self, body):
        while (True):
            apple_poscheck = False
            self.xpos = random.randint(0, 19) * self.width
            self.ypos = random.randint(0, 19) * self.width    
            for node in body:
                if self.xpos != node.xpos and self.ypos != node.ypos:
                    apple_poscheck = True
            if apple_poscheck == True:
                break
    def draw(self):
        pg.draw.rect(gameDisplay ,rect = pg.Rect(self.xpos,self.ypos, self.width, self.width), color=self.color)

# GAME LOOP
snake = Snake()
apple = Apple()
snake.spawn()
apple.spawn_first()
def restartGame():
    global snake, apple, score
    snake = Snake()
    apple = Apple()
    snake.spawn()
    apple.spawn_first()
    score = 0
while running:
    seconds_ticks = pg.time.get_ticks()
    dt=(seconds_ticks-start_ticks)/1000
    # Quit button
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    draw_text("Score: " + "{:04n}".format(score), 620, 100, (255,255,255))
    pg.display.flip()
    keys = pg.key.get_pressed()
    directions = [0 ,0, 0, 0]
    if keys[pg.K_UP]:
        snake.turn("U")
        directions[0] = 1
    if keys[pg.K_DOWN]:
        snake.turn("D")
        directions[1] = 1
    if keys[pg.K_LEFT]:
        snake.turn("L")
        directions[2] = 1
    if keys[pg.K_RIGHT]:
        snake.turn("R")
        directions[3] = 1
    drawDirection(gameDisplay, (255, 255, 255), (750, 400), 30, directions)
    if dt >= 0.08:
        gameDisplay.fill(back)
        drawGrid()
        apple.draw()
        snake.move()
        snake.draw()
        if snake.checkApplecollision(apple.xpos, apple.ypos): apple.spawn_aftereaten(snake.body)
        if snake.checkWallcollision(): 
            restartGame()
            continue
        start_ticks = seconds_ticks
    clock.tick()