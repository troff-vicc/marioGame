import pygame
class Question(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        question = pygame.image.load ('tecsture/question.png')
        self.question = pygame.transform.scale (question, (45, 45))
        question1 = pygame.image.load ('tecsture/question1.png')
        self.question1 = pygame.transform.scale (question1, (45, 45))
        question2 = pygame.image.load ('tecsture/question2.png')
        self.question2 = pygame.transform.scale (question2, (45, 45))
        self.image = self.question
        self.rect = self.image.get_rect ()
        self.last_update = 0
        self.rect.x = x * 45
        self.rect.y = y * 45
    def update(self):
        now = pygame.time.get_ticks ()
        time = 150
        if now - self.last_update > time and self.image == self.question:
            self.last_update = now
            self.image = self.question1
        elif now - self.last_update > time and self.image == self.question1:
            self.last_update = now
            self.image = self.question2
        elif now - self.last_update > time and self.image == self.question2:
            self.last_update = now
            self.image = self.question
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))