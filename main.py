import pygame as pg
import random
pg.init()


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
VELOCITY = 300
nrows = 20
ncols = 20 
grid_val = DISPLAY_HEIGHT / nrows
class Apple():
    def __init__(self, width) -> None:
        self.color = (255, 0, 0)
        self.width = width
    def spawn(self):
        self.xpos = random.randint(1, 10) * self.width
        self.ypos = random.randint(1, 10) * self.width
    def draw(self):
        pg.draw.rect(gameDisplay ,rect = pg.Rect(self.xpos,self.ypos, self.width, self.width), color=self.color)

class Node():
    def __init__(self, width, zone_width, zone_height):
        self.color = (0, 255, 0)
        self.width = width
        self.velocity = 300
        self.direction = "R"
        self.wallL = 0
        self.wallU = 0
        self.wallR = zone_width
        self.wallD = zone_height
    def spawn(self):
        self.xpos = random.randint(1, 10) * self.width
        self.ypos = random.randint(1, 10) * self.width
    def drawHead(self):
        pg.draw.rect(gameDisplay ,rect = pg.Rect(self.xpos,
                                                  self.ypos, self.width, self.width), color=self.color)
    def checkcollision(self, apple_xpos, apple_ypos):
        if (self.xpos == apple_xpos and self.ypos == apple_ypos):
            print("eat")
            return True
    def move(self, time):
        if (time >= 0.1):
            if self.direction == "U":
                if self.ypos > self.wallU:
                    self.ypos -= self.width
            if self.direction == "D":
                if self.ypos < self.wallD - self.width:
                    self.ypos += self.width
            if self.direction == "L":
                if self.xpos > self.wallL:
                    self.xpos -= self.width
            if self.direction == "R":
                if self.xpos < self.wallR - self.width:
                    self.xpos += self.width
            return True
        return False
    def turn(self, type):
        if type == "U" and self.direction != "D":
            self.direction = "U"
        if type == "D" and self.direction != "U":
            self.direction = "D"
        if type == "L" and self.direction != "R":
            self.direction = "L"
        if type == "R" and self.direction != "L":
            self.direction = "R"

class Snake():
    def __init__(self) -> None:
        self.body = [Node(grid_val, DISPLAY_HEIGHT, DISPLAY_HEIGHT)]


def drawGrid():
    for i in range(nrows + 1):
        pg.draw.line(gameDisplay, (255, 255, 255, 255),
                     (0, i * grid_val), (DISPLAY_HEIGHT, i * grid_val))
    for i in range(ncols + 1):
        pg.draw.line(gameDisplay, (255, 255, 255, 255),
                     (i * grid_val, 0), (i * grid_val, DISPLAY_HEIGHT))
back = (0, 0, 0)

gameDisplay = pg.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pg.display.set_caption('Snake AI')
gameDisplay.fill(back)
clock = pg.time.Clock()
start_ticks = pg.time.get_ticks()
running = True

snake = Snake()
apple = Apple(grid_val)
snake.spawn()
apple.spawn()
while running:
    seconds = pg.time.get_ticks()
    dt=(seconds-start_ticks)/1000
    # Quit button
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Check pressed key
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
    snake.drawHead()

    if snake.move(dt): start_ticks = seconds
    if snake.checkcollision(apple.xpos, apple.ypos): apple.spawn()
    apple.draw()





    # pg.display.update()
    pg.display.flip()

pg.quit()
quit()