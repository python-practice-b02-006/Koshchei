import pygame as pg
import numpy as np
from random import randint
SCREEN_SIZE = (680, 600)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
pg.init()
class Ball():
    """
    Creates balls, manages their movement, collisions, rendering.
    """
    def __init__(self, coord, vel, rad=20, color=None):
        """
        Creates a ball with given initial conditions.
        """
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        """
        Draws the ball on the screen.
        """
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self, t_step=1., g=2.):
        """
        Moves the ball. Velocity of the ball is also changed due to gravity.
        """
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
               self.is_alive = False

    def check_walls(self):
        """
        Checks if the ball has collided with walls and calls flip_vel method to change its velocity if it did.
        """
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i], 0.8, 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i], 0.8, 0.9)

    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        """
        Changes the velocity of the ball as if it collided inelastically with a wall with normal vector "axis".
        """
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist() 
class Table():
    """
    Manages counting of points and showing them to th player.
    """
    def __init__(self, shoots_in_trgt=0, shoots=0):
        self.shoots_in_trgt = shoots_in_trgt
        self.shoots = shoots
        self.font = pg.font.SysFont("garamondкурсив", 25)

    def score(self):
        return 2*self.shoots_in_trgt - self.shoots

    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Колличество лаб, сданных на полный балл: {}".format(self.shoots_in_trgt), 
                                           True, WHITE))
        score_surf.append(self.font.render("Shoots: {}".format(self.shoots), True, WHITE))
        score_surf.append(self.font.render("Score: {}".format(self.score()), True, RED))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])    
class Gun():
    """
    Creates a gun, manages its movement, shooting, aiming and rendering.
    """
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], min_pow=10, max_pow=60):
        """
        Creates a gun with given initial conditions.
        """
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False
    def draw(self, screen):
        """
        Draws a gun on the screen.
        """
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 10)
    def strike(self):
        """
        Creates a ball. Velocity of the ball depends on where the gun is pointing and how much power it has.
        """
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
        
    def move(self):
        """
        Increases the gun's power.
        """
        if self.active and self.power < self.max_pow:
            self.power += 2
    def set_angle(self, mouse_pos):
        """
        Changes the angle of the gun.
        """
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])
class Target():
    """
    Creates targets, manages their collisions with balls, rendering.
    """
    def __init__(self, coord = None, color = None, rad = 30):
        """
        Creates a target with given initial conditions.
        """
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
        """
        Checks if the ball collided with the target.
        """
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist
        

    def draw(self, screen):
        """
        Draws the target on the screen.
        """
        pg.draw.circle(screen, self.color, self.coord, self.rad)
    
class Obstacle():
    def __init__(self, coord = None, color = None, S = 20, H = 90, speed = randint(-10, 10)):
        """Creates an obstacle.
        :param height: height of the obstacle.
        :param width: width of the obstacle.
        :param coord: coordinates of the center of the obstacle.
        :param color: color of the obstacle.
        """
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
        """
        Moves the obstacle.
        """
        self.coord[1] += self.speed
        if self.coord[1] + self.height > SCREEN_SIZE[1] or self.coord[1] < 0:
            self.speed = -self.speed
        
    def draw(self, screen):
        """
        Draws the obstacle on the screen.
        """
        surf = pg.Surface((self.height, self.width))
        surf.fill(RED)
        f = pg.font.SysFont('arial', 26)
        text = f.render('SEREGA', 0, (255, 255, 255))
        surf.blit(text, (0, -5))
        surf2 = pg.transform.rotate(surf, 90)
        
        screen.blit(surf2, (self.coord[0], self.coord[1]))
        

class Manager():
    """
    Manages the process of the game.
    """
    def __init__(self, n_targets = 1, n_obstacles = 1):
        """
        Creates a game: guns, balls, targets and a score table. Creates variables to monitor the state of the game.
        """
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
        """
        Create new targets.
        """
        for i in range(self.n_targets):
            self.targets.append(Target(rad=randint(20, 30)))
            
    def set_obstacles(self):
        """
        Create new obstacles.
        """
        for i in range(self.n_obstacles):
            self.obstacles.append(Obstacle())
        
    def process(self, events, screen):
        """
        Manages the game. If all the targets have been hit, creates new ones.
        """
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
        """
        Draws all the objects, which have to drawn on the screen.
        """
        screen.fill(BLACK)
        SC_IMG = pg.image.load("Поставьте пожалмста полный балл.jpeg")
        screen.blit(SC_IMG, (0, 0))
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.gun.draw(screen)
        self.table.draw(screen)
        
        
        
    def move(self):
        """
        Moves all the objects, which have to be moved.
        """
        for ball in self.balls:
            ball.move()
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.move()
        self.gun.move()
        
        
    def collide(self):
        """
        Checks if the balls have hit some targets.
        """
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
                if (obstacle.coord[1] - ball.rad < ball.coord[1] < obstacle.coord[1] + obstacle.height + ball.rad 
                    and obstacle.coord[0] - ball.rad < ball.coord[0] < obstacle.coord[0] + obstacle.width + ball.rad): 
                    ball.coord[1] = SCREEN_SIZE[1] - ball.rad
                    ball.vel[1] = 0
                    
        for j in reversed(targets_c):
            self.table.shoots_in_trgt += 1
            self.targets.pop(j)

    def check_alive(self):
        """
        Checks if the balls are still moving and if the targets have not been hit yet.
        """
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.is_alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)

    def handle_events(self, events):
        """
        Handles the events.
        """
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
pg.display.set_caption("Поставьте пожалмста полный балл")


clock = pg.time.Clock()
mgr = Manager(n_targets=5, n_obstacles = 3)
done = False
SC_IMG = pg.image.load("Поставьте пожалмста полный балл.jpeg")
screen.blit(SC_IMG, (0, 0))
while not done:
    
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
    
pg.quit()
