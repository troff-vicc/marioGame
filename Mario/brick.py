import pygame
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        brick = pygame.image.load ('tecsture/brick.png')
        brick = pygame.transform.scale (brick, (45, 45))
        self.image = brick
        self.rect = self.image.get_rect ()
        self.rect.x = x * 45
        self.rect.y = y * 45
    def update(self, key):
        pass
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))