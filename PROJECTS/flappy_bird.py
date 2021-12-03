import pygame
import random

pygame.init()

class Game():
    def __init__(self):
        self.resolution = (500,500)
        self.screen = pygame.display.set_mode(self.resolution)
        self.title = "Flappy Bird"
        self.run = True
        self.fps_clock = pygame.time.Clock()
        self.fps = 50

game = Game()

class Bird():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.gravity = 0
        self.jump = 10
    def fall(self):
        if self.y < game.resolution[1]-self.radius:
            self.gravity += 1
        else:
            self.gravity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -self.jump
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.gravity = -self.jump
        self.y += self.gravity
    def draw(self):
        self.rect = pygame.draw.circle(game.screen, self.color, (int(self.x), int(self.y)), self.radius)

bird = Bird(int(game.resolution[0]/2), int(game.resolution[1])/2, 20, (255,0,0))

class Tube():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
    def move(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = game.resolution[0]
            self.y = game.resolution[1]-150
    def colide(self):
            if self.rect.colliderect(bird.rect):
                self.speed = 0
                bird.gravity = 0
            else:
                self.speed = 5
    def draw(self): 
        self.rect = pygame.draw.rect(game.screen, self.color, (self.x, self.y, self.width, self.height))
            
tube = Tube(game.resolution[0], game.resolution[1]-150, 75, 150, (25,100,25))

while game.run:
    game.screen.fill((0,175,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False
    bird.draw()
    bird.fall()
    tube.draw()
    tube.move()
    tube.colide()
    game.fps_clock.tick(game.fps)
    pygame.display.update()