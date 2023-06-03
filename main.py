import pygame as pg
import random
pg.init()

back = (0, 0, 0)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
nrows = 20
ncols = 20 
grid_val = DISPLAY_HEIGHT / nrows
score = 0
gameDisplay = pg.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pg.display.set_caption('Snake AI')
gameDisplay.fill(back)
running = True
clock = pg.time.Clock()
start_ticks = pg.time.get_ticks()




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
        self.body = [Node((0,255,0))]
        self.direction = "R"
        self.width = grid_val
    def spawn(self):
        self.body[0].xpos = 30
        self.body[0].ypos = 30
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
while running:
    seconds_ticks = pg.time.get_ticks()
    dt=(seconds_ticks-start_ticks)/1000
    # Quit button
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    pg.display.flip()
    if dt >= 0.08:
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            snake.turn("U")
        if keys[pg.K_DOWN]:
            snake.turn("D")
        if keys[pg.K_LEFT]:
            snake.turn("L")
        if keys[pg.K_RIGHT]:
            snake.turn("R")

        gameDisplay.fill(back)
        drawGrid()
        if snake.checkApplecollision(apple.xpos, apple.ypos): apple.spawn_aftereaten(snake.body)
        apple.draw()
        snake.move()
        if snake.checkWallcollision(): running = False
        snake.draw()
        start_ticks = seconds_ticks

