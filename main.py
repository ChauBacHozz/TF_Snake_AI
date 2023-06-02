import pygame as pg
pg.init()


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
nrows = 20
ncols = 20 
grid_val = DISPLAY_HEIGHT / nrows
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


while running:
    # Quit button
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    xpos += 1
    ypos += 1
    print(xpos)
    gameDisplay.fill(back)
    drawGrid()
    # pg.draw.rect(gameDisplay ,rect = pg.Rect(xpos, ypos, 100, 100), color=(255, 0, 0))






    # pg.display.update()
    pg.display.flip()
    clock.tick(60)   

pg.quit()
quit()