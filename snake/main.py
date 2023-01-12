import pygame 
from pygame.locals import *
import time

IMG_SIZE = 40

def foo(a):
    print(a)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen.fill((140, 68, 98))
        self.player = Entity(self.screen)
        self.player.render_obj()


    def run(self):
        status = True

        last_direction = K_0

        while status:

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    print(event.key)
                    move_foo = keys.get(event.key, False)
                    if move_foo:
                        move_foo()
                        self.player.render_obj()

                    if event.key == K_ESCAPE:
                        status = False
                    
                    last_direction = event.key
            
            self.player.auto_walk(last_direction)
            time.sleep(0.3)

class Entity:

    def __init__(self, screen, src='snake/resources/me.png', x=15, y=15, length=3):
        self.x = [IMG_SIZE]*length
        self.y = [IMG_SIZE]*length
        self.screen = screen
        self.texture = pygame.image.load(src).convert()
        self.snake_size = length

    ## yeah this makes not using a if to selection but feels cluncky right?
    def move_d(self, dx=10):
        self.x[0] += dx 
        for i in range(self.snake_size - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


    def move_a(self, dx=10):
        self.x[0] -= dx
        for i in range(self.snake_size - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def move_s(self, dx=10):
        self.y[0] += dx
        for i in range(self.snake_size - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def move_w(self, dx=10):
        self.y[0] -= dx
        for i in range(self.snake_size - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
    ## 

    def render_obj(self):
        self.screen.fill((140, 68, 98))
        for i in range(self.snake_size):
            self.screen.blit(self.texture, (self.x[i], self.y[i]))
        pygame.display.flip()


    def auto_walk(self, key): 
        move_foo = keys.get(key, False)
        if move_foo:
            move_foo(dx=25)
            self.render_obj()

    def get_pos(self):
        return self.x , self.y


if __name__ == "__main__":

    game = Game()
    keys = {97 : game.player.move_a , 115 : game.player.move_s, 100 : game.player.move_d, 119: game.player.move_w}
    game.run()

