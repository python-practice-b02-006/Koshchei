import numpy as np
import pygame 
from random import randint, gauss

pygame.init()
SCREEN_SIZE = (700, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("The gun of Khirianov")
random_color = (randint(0, 255), randint(0, 255), randint(0,255))
BLACK = (0, 0, 0)

class Gun():
    pass



class Table():
    pass


class Ball():
    pass


class Target():
    pass




class Manager():
    def __init__(self):
        self.gun = Gun()



        self.table = Table()

    def process(self, events, screen):
        done = self.handle_events(events)

        self.draw(screen)

        return done


    def draw(self, screen):
        screen.fill(BLACK)

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
        return done

done = False
clock = pygame.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)


    done = mgr.process(pygame.event.get(), screen)

    pygame.display.flip()


pygame.quit()
