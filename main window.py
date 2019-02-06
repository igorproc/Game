import pygame
import os

pygame.init()

size = width, height = 400, 800
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image('1.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 33
        self.rect.y = 33


all_sprites = pygame.sprite.Group()
Hero(all_sprites)

clock = pygame.time.Clock()
hero = Hero
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.rect -= 10
    elif keys[pygame.K_RIGHT]:
        print('право')
    elif keys[pygame.K_DOWN]:
        print('низ')
    elif keys[pygame.K_UP]:
        print('низ')
    screen.fill(pygame.Color(255, 186, 222))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
