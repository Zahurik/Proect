import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 250
        self.y = 250
        
    def draw(self):
        pg.draw.circle(self.screen, 'black', (self.x, self.y), 25)

    def move(self, keys):
        if keys[pg.K_w]:
            self.y -= 10
        if keys[pg.K_s]:
            self.y += 10
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10

    def update(self):
        pass