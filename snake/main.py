import pygame 
from pygame.locals import *
import time
from random import randint

IMG_SIZE = 50
SCREEN_SIZE = 800
# BACKGROUND_COLOR = (50,90,23)
BACKGROUND_COLOR = (0,0,0)


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
        self.score = 0

    def main_menu(self, is_lost=False):
        
        pygame.font.init()

        self.screen.fill((0,0,0))
        pygame.display.flip()

        myfont = pygame.font.SysFont("monospace", 20)
        intro_text = "Press F1 to start or ESC to leave"

        if is_lost:
            intro_text = f"Game Over! Score: {self.score}"

        label = myfont.render(intro_text, 1, (255,255,255))

        text_rect = label.get_rect(center=(SCREEN_SIZE/2, SCREEN_SIZE/2))
        
        self.screen.blit(label, text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_F1:
                        return not is_lost  
                    
                    if event.key == K_ESCAPE:
                        return False

    def show_score(self):
        font = pygame.font.SysFont("monospace", 20)
        score = font.render(f"Score : {self.score}", 1, (255,255,255))
        self.screen.blit(score, (SCREEN_SIZE * 0.8, 0))


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

            if self.player.out_of_bounds():
                status = False


            if self.player.is_colliding(x,y):
                self.score += 1
                self.wheys.change_pos()
                self.player.increase_snake()
                # contar score, apagar o whey e renderizar outro, aumentar uma cobra


            self.player.move_player(last_direction)
            self.wheys.render_obj()
            self.show_score()
            pygame.display.flip()
            time.sleep(0.3)
    
        self.main_menu(is_lost=True)


class Entity:

    def __init__(self, screen, src='snake/resources/me.png', x=0, y=0):
        self.x = x
        self.y = y
        self.screen = screen
        self.texture = pygame.image.load(src).convert()

    def render_obj(self):
        self.screen.fill(BACKGROUND_COLOR)    
        self.screen.blit(self.texture, (self.x, self.y))
        # pygame.display.flip()

    def compare_pos(self, x1, y1):
        return self.x == x1 and self.y == y1


class Whey(Entity):
    
    def __init__(self, screen, src='snake/resources/whey.png', x=4, y=4):
        self.x = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE
        self.y = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE

        super().__init__(screen, src, self.x, self.y)

    def render_obj(self):
        self.screen.blit(self.texture, (self.x, self.y))
        pygame.display.flip()
    
    def get_pos(self):
        return (self.x, self.y)

    def change_pos(self):

        new_x = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE
        new_y = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE

        while self.compare_pos(new_x, new_y):
            new_x = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE
            new_y = randint(1, (SCREEN_SIZE/IMG_SIZE) - 1) * IMG_SIZE

        self.x = new_x
        self.y = new_y

        self.render_obj()

class Snake(Entity):

    def __init__(self, screen, src='snake/resources/m3.png', head_text= 'snake/resources/m2.png', x=15, y=15, length=2):
        super().__init__(screen, src, [IMG_SIZE] * length, [IMG_SIZE] * length)
        self.snake_size = length
        self.head_texture = pygame.image.load(head_text).convert()
        

    def render_obj(self):
        self.screen.fill(BACKGROUND_COLOR)

        self.screen.blit(self.head_texture, (self.x[0], self.y[0]))

        for i in range(2, self.snake_size):
            self.screen.blit(self.texture, (self.x[i], self.y[i]))

        pygame.display.flip()


    def is_colliding(self, x, y):
        
        if self.x[0] >= x and self.x[0] <= x + IMG_SIZE*.9 and self.y[0] >= y and self.y[0] <= y + IMG_SIZE*.9:
            return True

        return False

    def out_of_bounds(self):
        if self.x[0] < 0 or self.x[0] > SCREEN_SIZE or self.y[0] < 0 or self.y[0] > SCREEN_SIZE:
            return True
        return False

    def move_player(self, direction, dx = IMG_SIZE):

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
        
    def increase_snake(self):
        self.x.append(-1)
        self.y.append(-1)
        self.snake_size += 1


if __name__ == "__main__":

    game = Game()
    game.run(game.main_passed)

