import pygame 
from pygame.locals import *
import time
from random import randint

IMG_SIZE = 40

def foo(a):
    print(a)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen.fill((140, 68, 98))
        self.player = Snake(self.screen)
        self.player.render_obj()
        self.wheys = Whey(self.screen)
        # self.wheys.render_obj()


    def run(self):
        status = True

        last_direction = K_0

        while status:

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    move_foo = keys.get(event.key, False)
                    if move_foo:
                        move_foo()
                        self.player.render_obj()
                        # self.wheys.render_obj()

                    if event.key == K_ESCAPE:
                        status = False
                    
                    last_direction = event.key
            
            # self.player.auto_walk(last_direction)
            # self.wheys.render_obj()
            time.sleep(0.9)



class Entity:

    def __init__(self, screen, src='snake/resources/me.png', x=15, y=15):
        self.x = x
        self.y = y
        self.screen = screen
        self.texture = pygame.image.load(src).convert()

    def render_obj(self):
        self.screen.fill((140, 68, 98))    
        self.screen.blit(self.texture, (self.x, self.y))
        pygame.display.flip()

    def compare_pos(self, x1, y1):
        return self.x == x1 and self.y == y1


class Whey(Entity):
    def __init__(self, screen, src='snake/resources/whey.png', x=4, y=4):
        
        x = randint(1, 250) * x
        y = randint(1, 200) * y

        super().__init__(screen, src, x, y)


    

class Snake(Entity):

    def __init__(self, screen, src='snake/resources/me.png', x=15, y=15, length=3):
        super().__init__(screen, src, [IMG_SIZE] * length, [IMG_SIZE] * length)
        self.snake_size = length

    def render_obj(self):
        self.screen.fill((140, 68, 98))
        for i in range(self.snake_size):
            self.screen.blit(self.texture, (self.x[i], self.y[i]))

        pygame.display.flip()

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


    def auto_walk(self, key): 
        move_foo = keys.get(key, False)
        if move_foo:
            move_foo(dx=25)
            self.render_obj()

if __name__ == "__main__":

    game = Game()
    keys = {97 : game.player.move_a , 115 : game.player.move_s, 100 : game.player.move_d, 119: game.player.move_w}
    game.run()

