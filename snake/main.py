import pygame 
from pygame.locals import *
import time
from random import randint

IMG_SIZE = 40
SCREEN_SIZE = 600

def foo(a):
    print(a)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.main_passed = self.main_menu()
        self.player = Snake(self.screen)
        self.player.render_obj()
        self.wheys = Whey(self.screen)
        self.wheys.render_obj()


    def main_menu(self):
        
        pygame.font.init()

        self.screen.fill((0,0,0))
        pygame.display.flip()

        myfont = pygame.font.SysFont("monospace", 20)
        intro_text = "Press F1 to start or ESC to leave"
        label = myfont.render(intro_text, 1, (255,255,255))

        text_rect = label.get_rect(center=(SCREEN_SIZE/2, SCREEN_SIZE/2))
        
        self.screen.blit(label, text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_F1:
                        return True   
                    
                    if event.key == K_ESCAPE:
                        return False



    def run(self, main_passed):
        status = main_passed
        last_direction = K_0

        while status:
            
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    
                    self.player.move_player(event.key)

                    if event.key == K_ESCAPE:
                        status = False
                    
                    last_direction = event.key

            x, y = self.wheys.get_pos()

            if self.player.is_colliding(x,y):
                print('encostou')
                # contar score, apagar o whey e renderizar outro, aumentar uma cobra
            else:
                time.sleep(.1)
                print("minhoca", x,y)
                print("maça",self.player.x[0],self.player.y[0] )

            self.player.move_player(last_direction)
            self.wheys.render_obj()
            time.sleep(0.3)



class Entity:

    def __init__(self, screen, src='snake/resources/me.png', x=0, y=0):
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
        self.x = randint(10, (SCREEN_SIZE/4) - 10) * x
        self.y = randint(10, (SCREEN_SIZE/4) - 10) * y

        super().__init__(screen, src, self.x, self.y)

    def render_obj(self):
        self.screen.blit(self.texture, (self.x, self.y))
        pygame.display.flip()
    
    def get_pos(self):
        return (self.x, self.y)


class Snake(Entity):

    def __init__(self, screen, src='snake/resources/minhoca.png', x=15, y=15, length=4):
        super().__init__(screen, src, [IMG_SIZE] * length, [IMG_SIZE] * length)
        self.snake_size = length

    def render_obj(self):
        self.screen.fill((140, 68, 98))
        for i in range(self.snake_size):
            self.screen.blit(self.texture, (self.x[i], self.y[i]))

        pygame.display.flip()


    def is_colliding(self, x, y):
        
        if self.x[0] >= x and self.x[0] <= x + IMG_SIZE and self.y[0] >= y and self.y[0] <= y + IMG_SIZE:
            return True

        return False

    def move_player(self, direction, dx = 40):

        if direction == 97:
            self.x[0] -= dx

        elif direction == 100:
            self.x[0] += dx

        elif direction == 115:
            self.y[0] += dx

        elif direction == 119:
            self.y[0] -= dx

        for i in range(self.snake_size - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        self.render_obj()
        

if __name__ == "__main__":

    game = Game()
    game.run(game.main_passed)

