import pygame 
from pygame.locals import *



def foo(a):
    print(a)



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.screen.fill((140, 68, 98))
        self.player = Entity(self.screen)
        self.player.render_obj()


    def run(self):
        status = True

        while status:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    try:
                        move_foo = keys[event.key]
                        move_foo()
                        self.player.render_obj()

                    except KeyError:
                        pass

                    if event.key == K_ESCAPE:
                        status = False



class Entity:

    def __init__(self, screen, src='resources/me.png', x=15, y=15):
        self.x = x
        self.y = y
        self.screen = screen
        self.texture = pygame.image.load(src).convert()

    # yeah this makes not using a if to selection but feels cluncky right?
    def move_d(self, dx=10):
        self.x += dx

    def move_a(self, dx=10):
        self.x -= dx

    def move_s(self, dx=10):
        self.y += dx

    def move_w(self, dx=10):
        self.y -= dx
    ## 

    def render_obj(self):
        self.screen.fill((140, 68, 98))
        self.screen.blit(self.texture, (self.x, self.y))
        pygame.display.flip()

    def get_pos(self):
        return self.x , self.y


if __name__ == "__main__":

    game = Game()
    keys = {97 : game.player.move_a , 115 : game.player.move_s, 100 : game.player.move_d, 119: game.player.move_w}
    game.run()

