import pygame, physics
from mario import Mario
from brick import Brick
from question import Question
from ground import Ground

class Game:
    def completionSprite(self, matrix):
        for y in range (len (matrix)):
            for x in range (len (matrix[y])):
                if matrix[y][x] == 1:
                    self.brick_group.add(Ground (x, y))
                elif matrix[y][x] == 2:
                    self.brick_group.add(Brick (x, y))
                elif matrix[y][x] == 3:
                    self.question_group.add(Question (x, y))
    def __init__(self):
        pygame.display.set_caption ("Mario")
        self.mario = Mario ()
        self.brick_group = pygame.sprite.Group()
        self.question_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group ()
        matrix = physics.main()
        self.completionSprite(matrix)
        self.screen = pygame.display.set_mode ((720, 720))
        self.clock = pygame.time.Clock ()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    running = False
            self.update ()
            self.draw ()
            pygame.display.update ()
            self.clock.tick (60)
    def update(self):
        self.mario.update(pygame.key.get_pressed())
        self.question_group.update()
    def draw(self):
        self.screen.fill ((157, 155, 255))
        self.mario.draw(self.screen)
        self.brick_group.draw(self.screen)
        self.question_group.draw (self.screen)
        self.ground_group.draw (self.screen)