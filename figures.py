from random import randint
import pygame as pg
import main
W = 400
H = 400
WHITE = (250, 250, 250)
class RECTANGLE:
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

        sc = pg.display.set_mode((W, H))

        kvadrat1 = RECTANGLE(randint(1, W))

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            main.exit()
 
    sc.fill(WHITE)
    sc.blit(kvadrat1.image, kvadrat1.rect)
    pg.display.update()
    pg.time.delay(20)

    if RECTANGLE.rect.y < d:

        RECTANGLE.rect.y += 2
    else:
        RECTANGLE.rect.y = 0