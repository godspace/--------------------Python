import pygame

class Game():
    def __init__(self):
        self.resolution = (800,600)
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
    def move(self):
        self.rect = pygame.draw.circle(game.screen, self.color, (self.x, self.y), self.radius)
        if self.y < game.resolution[1]:
            self.gravity += 1
        else:
            self.gravity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print(True)
            self.gravity = -20
        self.y += self.gravity


bird = Bird(int(game.resolution[0]/2), int(game.resolution[1]/2), 20, (255,0,0))

while game.run:
    game.screen.fill((0,175,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False
    bird.move()
    game.fps_clock.tick(game.fps)
    pygame.display.update()
