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


hscore = []
score = 0

#read scores history
out = open('score.txt', 'r')
for a in range (0, 5):
     hscore.append(int(out.readline()))
out.close()


#ball characteristics
n = 10 #number of balls
r = [] #radius
u = 10 
x = [] #coordinate x
y = [] #coordinate y
ux = [] #speed x
uy = [] # speed y
color = []
for i in range(n):
    x.append(randint(100, 700))
    y.append(randint(100, 500))
    r.append(randint(30, 70))
    ux.append(randint(-u, u))
    uy.append(randint(-u, u))
    color.append(COLORS[randint(0,4)])


def ball():
    global x, y, r, ux, uy, color
    a = 0
    while a < n:
        if color[a] == BLACK:
            color[a] = COLORS[randint(0, 4)]
            r[a] = randint(20, 40)
            x[a] = randint(r[a], l -r[a])
            y[a] = randint(r[a], h - r[a])
            ux[a] = randint(-u, u)
            uy[a] = randint(-u, u)
        x[a] = x[a] + ux[a]
        y[a] = y[a] + uy[a]
        if x[a] + r[a] >= l or x[a] - r[a] <= 0:
            ux[a] = -1 * ux[a]
        if y[a] + r[a] >= h or y[a] - r[a] <= 0:
            uy[a] = -1 * uy[a]
        circle(screen, color[a], (int(x[a]), int(y[a])), int(r[a]))
        a += 1
        
#square characteristics
ns = 5 #number of squares  
us = 20 
xs = [] #coordinate x
ys = [] #coordinate y
uxs = [] #speed x
uys = [] #speed y
m = 60 #width of square
colors = [] 
for i in range(ns):
    xs.append(randint(100, 700))
    ys.append(randint(100, 500))
    uxs.append(randint(-us, us))
    uys.append(randint(-us, us))
    colors.append(RED)


def square():
    global ns, us, xs, ys, uxs, uys, m, colors
    a = 0
    while a < ns:
        if colors[a] == BLACK:
            colors[a] = RED
            xs[a] = randint(m, l - m)
            ys[a] = randint(m, h - m)
            uxs[a] = randint(-us, us)
            uys[a] = randint(-us, us)
        xs[a] = xs[a] + uxs[a]
        ys[a] = ys[a] + np.sin(xs[a])*uys[a] + uys[a]
        if xs[a] + m >= l or xs[a] <= 0:
            uxs[a] = -1 * uxs[a]
        if ys[a] + m >= h or ys[a] <= 0:
            uys[a] = -1 * uys[a]
        rect(screen, colors[a], (int(xs[a]), int(ys[a]), m, m), 0)
        a += 1
        

 
#count scores       
def click(event):
    global score, u, m, k
    for i in range(0, n):
        if (event.pos[0] - x[i])**2 + (event.pos[1] - y[i])**2 <= r[i]**2:
            score += 1
            r[i] = 0
            color[i] = BLACK 
            u += 1
    for i in range(0, ns):
        if (event.pos[0] - xs[i] <= m and event.pos[1] - ys[i] <= m and 
            event.pos[0] - xs[i] >= 0 and event.pos[1] - ys[i] >= 0 ):
            score += 2
            colors[i] = BLACK
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
    ball()
    counter()
    square()
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
