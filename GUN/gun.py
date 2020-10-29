import pygame as pg
import numpy as np
from random import randint
SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
pg.init()
class Ball():
    def __init__(self, coord, vel, rad=20, color=None):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self, t_step=1., g=2.):
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
               self.is_alive = False

    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i], 0.8, 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i], 0.8, 0.9)

    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist() 
class Table():
   
    def __init__(self, shoots_in_trgt=0, shoots=0):
        self.shoots_in_trgt = shoots_in_trgt
        self.shoots = shoots
        self.font = pg.font.SysFont("garamondкурсив", 25)

    def score(self):
        return 2*self.shoots_in_trgt - self.shoots

    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Shoots in target: {}".format(self.shoots_in_trgt), 
                                           True, WHITE))
        score_surf.append(self.font.render("Shoots: {}".format(self.shoots), True, WHITE))
        score_surf.append(self.font.render("Score: {}".format(self.score()), True, RED))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])    
class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], 
                 min_pow=10, max_pow=60):
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False
    def draw(self, screen):
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 10)
    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
        
    def move(self):
        if self.active and self.power < self.max_pow:
            self.power += 2
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])
class Target():
    def __init__(self, coord = None, color = None, rad = 30):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        for i in range(2):
            gun_coord=[30, SCREEN_SIZE[1]//2]
            while coord[i] - gun_coord[i] < 80 and gun_coord[i] - coord[i] < 80:
                coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.color = color
        self.coord = coord
        self.rad = rad
        
    def check_collision(self, ball):
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist
        
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
    
class Obstacle():
    def __init__(self, coord = None, color = None, S = 10, H = 60, speed = randint(-10, 10)):
        if color == None:
            color = RED
        if coord == None:
            coord = [randint(80, SCREEN_SIZE[0] - 100), randint(0, SCREEN_SIZE[1] - H)]
        self.color = color
        self.coord = coord
        self.speed = speed
        self.width = S
        self.height = H
        
    def move(self):
        self.coord[1] += self.speed
        if self.coord[1] + self.height > SCREEN_SIZE[1] or self.coord[1] < 0:
            self.speed = -self.speed

        
    def check_collision(self, ball):
        dist = np.sqrt((self.coord[0] - ball.coord[0])**2 + (self.coord[1] + 40 - ball.coord[1])**2)
        min_dist = 3*ball.rad
        return dist <= min_dist
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.coord[0], self.coord[1], self.width, self.height))

class Manager():
    def __init__(self, n_targets = 1, n_obstacles = 1):
        self.gun = Gun()
        self.table = Table()
        self.balls = []
        self.targets = []
        self.obstacles = []
        self.table = Table()
        self.n_targets = n_targets
        self.n_obstacles = n_obstacles 
        self.new_mission()
        
    def new_mission(self):
        for i in range(self.n_targets):
            self.targets.append(Target(rad=randint(20, 30)))
            
    def set_obstacles(self):
        for i in range(self.n_obstacles):
            self.obstacles.append(Obstacle())
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.collide()
        self.draw(screen)
        self.check_alive()
        if len(self.obstacles) == 0:
            self.set_obstacles()
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()
        return done

    def draw(self, screen):
        screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.gun.draw(screen)
        self.table.draw(screen)
        
        
        
    def move(self):
        for ball in self.balls:
            ball.move()
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.move()
        self.gun.move()
        
        
    def collide(self):
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for i, ball in enumerate(self.balls):
            for j, obstacle in enumerate(self.obstacles):
                if obstacle.check_collision(ball):
                    n = [[1, 0], [0, 1]]
                    ball.coord[0] -= ball.vel[0]
                    ball.flip_vel(n[0])
        for j in reversed(targets_c):
            self.table.shoots_in_trgt += 1
            self.targets.pop(j)

    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.is_alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 5
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 5
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    self.table.shoots += 1
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Khiryanov")
clock = pg.time.Clock()
mgr = Manager(n_targets=5, n_obstacles = 3)
done = False
while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
pg.quit()
