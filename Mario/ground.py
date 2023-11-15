import pygame
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ground1 = pygame.image.load ('tecsture/ground.png')
        ground = pygame.transform.scale (ground1, (45, 45))
        self.image = ground
        self.rect = self.image.get_rect()
        self.rect.x = x * 45
        self.rect.y = y * 45
    def update(self, key):
        pass
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))