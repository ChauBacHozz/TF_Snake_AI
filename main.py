import pygame as pg
import random
pg.init()


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
VELOCITY = 300
nrows = 20
ncols = 20 
grid_val = DISPLAY_HEIGHT / nrows

class Snake():
    def __init__(self, width):
        self.nodes = 1
        self.color = (0, 255, 0)
        self.width = width
        self.velocity = 200
        self.direction = "R"
    def spawn(self):
        self.xpos = random.randint(1, 10) * 5
        self.ypos = random.randint(1, 10) * 5
    def drawHead(self):
        pg.draw.rect(gameDisplay ,rect = pg.Rect(round(self.xpos / self.width) * self.width
                                                 ,round(self.ypos / self.width) * self.width, self.width, self.width), color=self.color)
    def move(self, dt):
        if self.direction == "U":
            self.ypos -= self.velocity * dt
        if self.direction == "D":
            self.ypos += self.velocity * dt
        if self.direction == "L":
            self.xpos -= self.velocity * dt
        if self.direction == "R":
            self.xpos += self.velocity * dt
    def turn(self, type):
        if type == "U" and self.direction != "D":
            self.direction = "U"
        if type == "D" and self.direction != "U":
            self.direction = "D"
        if type == "L" and self.direction != "R":
            self.direction = "L"
        if type == "R" and self.direction != "L":
            self.direction = "R"
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
running = True
xpos = 0
ypos = 0

snake = Snake(grid_val)
snake.spawn()
while running:
    dt = clock.tick(60) / 1000
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
    snake.move(dt)
    snake.drawHead()





    # pg.display.update()
    pg.display.flip()

pg.quit()
quit()