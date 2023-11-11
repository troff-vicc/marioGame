import pygame
def moveMario(key, mario):
    if key[pygame.K_d]:
        if mario.rect.x < 680:
            mario.rect.x += mario.vx
    elif key[pygame.K_a]:
        if mario.rect.x > -5:
            mario.rect.x -= mario.vx
    return mario