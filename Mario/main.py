import pygame, physics, move
#   Создание переменных
WIDTH = 360
HEIGHT = 480
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (157,155,255)
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)

mario1 = pygame.image.load('tecsture/mario.png')
mario1 = pygame.transform.scale(mario1, (45, 45))

ground = pygame.image.load('tecsture/ground.png')
ground = pygame.transform.scale(ground, (45, 45))

question = pygame.image.load('tecsture/question.png')
question = pygame.transform.scale(question, (45, 45))

question1 = pygame.image.load('tecsture/question1.png')
question1 = pygame.transform.scale(question1, (45, 45))

question2 = pygame.image.load('tecsture/question2.png')
question2 = pygame.transform.scale(question2, (45, 45))

brick = pygame.image.load('tecsture/brick.png')
brick = pygame.transform.scale(brick, (45, 45))
#   Классы объектов
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mario1
        self.rect = self.image.get_rect()
        self.rect.x = 32 * 45 / 16
        self.rect.y = 192 * 45 / 16
        self.vx = 3.75
        self.vy = 3.75
class Sprite(pygame.sprite.Sprite):
    def __init__(self, meaning):
        pygame.sprite.Sprite.__init__(self)
        self.last_update = 0
        if meaning == 1:
            self.image = ground
            self.rect = self.image.get_rect()
            self.not0 = True
        if meaning == 2:
            self.image = brick
            self.rect = self.image.get_rect()
            self.not0 = True
        elif meaning == 3:
            self.image = question
            self.rect = self.image.get_rect()
            self.not0 = True
        else:
            self.not0 = False
    def update(self):
        now = pygame.time.get_ticks()
        time = 150
        if now - self.last_update > time and self.image == question:
            self.last_update = now
            self.image = question1
        elif now - self.last_update > time and self.image == question1:
            self.last_update = now
            self.image = question2
        elif now - self.last_update > time and self.image == question2:
            self.last_update = now
            self.image = question
#   Создание окна
pygame.init()
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Mario")

#   Создание спрайтов

all_sprites_list = pygame.sprite.Group()

matrix = physics.main()
listSprite = []
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        object = Sprite(matrix[y][x])
        if object.not0:
            object.rect.x = x * 45
            object.rect.y = y * 45
            listSprite.append(matrix[y][x])
            all_sprites_list.add(object)

mario = Mario()
mario_group = pygame.sprite.Group()
mario_group.add(mario)

clock = pygame.time.Clock()
running = True

#   Игровой цикл
while running:
    mario = move.moveMario(pygame.key.get_pressed(), mario)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    mario_group.draw(screen)
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()