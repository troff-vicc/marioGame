import pygame
from brick import Brick
from question import Question
from ground import Ground

class Mario():
    def __init__(self):
        mario1 = pygame.image.load ('tecsture/mario.png')
        mario1 = pygame.transform.scale (mario1, (45, 45))
        pygame.sprite.Sprite.__init__(self)
        self.image = mario1
        self.rect = self.image.get_rect()
        self.rect.x = 32 * 45 / 16
        self.rect.y = 192 * 45 / 16
        self.vx = 3.75
        self.vy = 3.75
    def update(self, key):
        if key[pygame.K_d]:
            if self.rect.x < 680:
                self.rect.x += self.vx
        elif key[pygame.K_a]:
            if self.rect.x > -5:
                self.rect.x -= self.vx
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))