import random
import sys

import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
score = 0


class snake(object):
    def __init__(self, facing):
        self.x = 200
        self.y = 200
        self.head = [self.x, self.y]
        self.pos = [[self.x, self.y], [self.x, self.y], [self.x, self.y], [self.x, self.y]]
        self.width = 20
        self.height = 20
        self.facing = facing

    def draw(self):                                 # make list of red boxes to represent Snake
        for p in self.pos:
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(p[0], p[1], self.width, self.height))

    def hit(self):
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('Game Over', 1, (255, 0, 0))

        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 5:
            pygame.time.delay(1000)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 6
                    pygame.quit()
        sys.exit(0)


class fruit(object):
    def __init__(self, radius):
        c = random.randrange(2, 40) * 10
        d = random.randrange(2, 40) * 10
        self.x = c
        self.y = d
        self.radius = radius
        self.pos = [self.x - 10, self.y - 10]

    def hit(self):
        c = random.randrange(2, 40) * 10
        d = random.randrange(2, 40) * 10
        self.x = c
        self.y = d
        self.pos = [self.x - 10, self.y - 10]
        pygame.display.update()

    def draw(self):
        pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), self.radius)


def redrawGameWindow():
    win.fill((0, 0, 0))
    s.draw()
    f.draw()
    text = font.render('Score: ' + str(score), 1, (0, 0, 255))
    win.blit(text, (350, 10))
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
s = snake(2)
f = fruit(10)
run = True
vel = 10

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # buttons setup
    if keys[pygame.K_LEFT] and s.facing != 2:
        s.facing = 1
    if keys[pygame.K_RIGHT] and s.facing != 1:
        s.facing = 2
    if keys[pygame.K_UP] and s.facing != 4:
        s.facing = 3
    if keys[pygame.K_DOWN] and s.facing != 3:
        s.facing = 4

    # Changing Direction
    if s.facing == 1:
        s.head[0] -= vel
    if s.facing == 2:
        s.head[0] += vel
    if s.facing == 3:
        s.head[1] -= vel
    if s.facing == 4:
        s.head[1] += vel

    # Snake hits wall
    if s.head[0] >= 500 - s.width or s.head[0] <= 0:
        s.hit()
        f.hit()
    elif s.head[1] >= 500 - s.height or s.head[1] <= 0:
        s.hit()
        f.hit()

    # Moving Animation
    s.pos.insert(0, list(s.head))                               # add red box on head of the list
    s.pos.pop()                                                 # remove red box from tail of the list

    # Snake hits itself
    s.head = s.pos[0]
    if s.head in s.pos[4:]:
        s.hit()

    # Snake takes Fruit
    if s.head[0] + 20 > f.pos[0] and s.head[0] < f.pos[0] + 20 and s.head[1] + 20 > f.pos[1] and s.head[1] < f.pos[
        1] + 20:
        f.hit()
        s.pos.insert(0, list(s.head))
        score = score + 1

    redrawGameWindow()

pygame.quit()
