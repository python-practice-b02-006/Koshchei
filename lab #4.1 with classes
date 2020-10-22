import pygame
import numpy as np
from pygame.draw import *
from numpy import *
from random import randint
pygame.init()

#colors
RED = (255, 0, 0)
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0) 
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
ROZOVYI_POSCHEKOCHI_MENYA = (252, 137, 172)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]


#video settings
l = 1200
h = 700
FPS = 60
screen = pygame.display.set_mode((l, h))



#ball characteristics
n = 10 #number of balls
u = 10


class Ball():
    def __init__(self):
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.ux = randint(-u, u)
        self.uy = randint(-u, u)
        self.r = randint(30, 70)
        self.color = COLORS[randint(0,4)]
    def move(self):
        if self.color == BLACK:
            self.color = COLORS[randint(0,4)]
            self.r = randint(30, 70)
            self.x = randint(self.r, l - self.r)
            self.y = randint(self.r, h - self.r)
            self.ux = randint(-u, u)
            self.uy = randint(-u, u)
        self.x += self.ux
        self.y += self.uy
        if self.x + self.r >= l or self.x - self.r <= 0:
            self.ux = -1 * self.ux
        if self.y + self.r >= h or self.y - self.r <= 0:
            self.uy = -1 * self.uy
        circle(screen, self.color, (int(self.x), int(self.y)), int(self.r))
    
        
#square charaacteristics
ns = 5 # number of squares
us = 20
m = 60 #width of square

class Square():
    def __init__(self):
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.ux = randint(-us, us)
        self.uy = randint(-us, us)
        self.color = RED
    def move(self):
        if self.color == BLACK:
            self.color = RED
            self.x = randint(m, l - m)
            self.y = randint(m, h - m)
            self.ux = randint(-us, us)
            self.uy = randint(-us, us)
        self.x += self.ux 
        self.y += self.uy + np.sin(self.x)*self.uy + np.cos(self.x)*self.uy
        if self.x + m >= l or self.x <= 0:
            self.ux = -1 * self.ux
        if self.y + m >= h or self.y <= 0:
            self.uy = -1 * self.uy
        rect(screen, self.color, (int(self.x), int(self.y), m, m), 0)
        
        
        
        
#init balls
ball = []  
for i in range (0, n):
    ball.append(Ball())      

#draw balls
def new_ball():
    for i in range (0, n): 
        ball[i].move()    

#init squares
square = []  
for i in range (0, ns): 
    square.append(Square())    
        
#draw bombs        
def new_square():
    for i in range (0, ns): 
        square[i].move()    
           
        
        
        

hscore = []
score = 0



#read scores history
out = open('score.txt', 'r')
for a in range (0, 5):
     hscore.append(int(out.readline()))
out.close()
        
        

#count scores       
def click(event):
    global score, u, m, k
    for i in range(0, n):
        if ((event.pos[0] - ball[i].x)**2 + (event.pos[1] - ball[i].y)**2
           <= ball[i].r**2):
            score += 1
            ball[i].r = 0
            ball[i].color = BLACK 
            u += 1
    for i in range(0, ns):
        if (event.pos[0] - square[i].x <= m and event.pos[1] - square[i].y <= m
            and event.pos[0] - square[i].x >= 0 and event.pos[1] - square[i].y >= 0 ):
            score += 2
            square[i].color = BLACK
            m -= 2


#print scores
def counter():
    surf = pygame.Surface((100, 30))
    surf.fill((0, 0, 0))
    rect(surf, ROZOVYI_POSCHEKOCHI_MENYA , (0,0, 100,30))
    font = pygame.font.Font(None, 25)
    text = font.render('Score: ' + str(score), True, WHITE)
    surf.blit(text, (10,5))
    screen.blit(surf, (0, 0))
    surf1 = pygame.Surface((100, 122))
    surf1.fill((0, 0, 0))
    font1 = pygame.font.Font(None, 20)
    
    line(surf1, WHITE, (0, 20), (100, 20), 3)
    rect(surf1, WHITE, (0, 0, 100, 120), 3)
    for i in range (1, 6):
        line(surf1, WHITE, (0, 20*(i + 1)), (100, 20*(i + 1)), 3)
        text = font1.render(str(hscore[i-1]), True, WHITE)
        surf1.blit(text, (10, 5 + 20*i))
    text = font1.render('HighScores', True, WHITE)
    surf1.blit(text, (10, 5))
    screen.blit(surf1, (l - 100, 0))
    
    
pygame.display.update()
clock = pygame.time.Clock()
FINISHED = False

while not FINISHED:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball()
    counter()
    new_square()
    pygame.display.update()
    screen.fill(BLACK)
           
#rewrite scores history
if score > hscore[4]: 
    print('Хорошая работа, Олег!')
    hscore[4] = score
hscore.sort(reverse = True)
inp = open('score.txt', 'w')
inp.flush()
for i in range(0, 5):
    inp.write(str(hscore[i]) + '\n')
inp.close()

print(score)
pygame.quit()
