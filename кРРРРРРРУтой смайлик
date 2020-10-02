

import pygame
import numpy as np

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
pygame.init()
sc = pygame.display.set_mode([1500, 800])
sc.fill(WHITE)

pygame.display.set_caption("Angry smile")

done = 0
clock = pygame.time.Clock()



#Лицо
pygame.draw.circle(sc, YELLOW, (250, 250), 200)
pygame.draw.circle(sc, BLACK, (250, 250), 201, 1)
    
#Глаза
pygame.draw.circle(sc, RED, (35*5, 35*5), 5*5)
pygame.draw.circle(sc, BLACK, (35*5, 35*5), 5*5+1, 1)
pygame.draw.circle(sc, BLACK, (35*5, 35*5 ), 2*5)
 
pygame.draw.circle(sc, RED, (65*5, 35*5), 4*5)
pygame.draw.circle(sc, BLACK, (65*5, 35*5), 4*5+1, 1)
pygame.draw.circle(sc, BLACK, (65*5, 35*5), 2*5)

#Рот
pygame.draw.line(sc, BLACK, [35*5, 65*5], 
                     [65*5, 65*5], 25) 
    

while done < 60:
    clock.tick(10)
        


    #Брови
    surface = pygame.Surface([40*5, 20*5], pygame.SRCALPHA)
    pygame.draw.line(surface, BLACK, [0,0], [38*5, 0], 20)
    surface_rot = pygame.transform.rotate(surface, 333)
    sc.blit(surface_rot, [2*5, 15*5+done])

    surface = pygame.Surface([40*5, 20*5], pygame.SRCALPHA)
    pygame.draw.line(surface, BLACK, [0,0], [35*5, 0], 18)
    surface_rot = pygame.transform.rotate(surface, 27)
    sc.blit(surface_rot, [56*5, 15*5+done])

    pygame.display.flip()
    done += 1

pygame.quit()
