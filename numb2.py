import tmx3
import random
import math
import tmx3
import random
import math
import pygame
from socket import *
from pygame.locals import *
from random import randint


pygame.init()
screen = pygame.display.set_mode((1024,640))
tilemap = tmx3.load('map.tmx', screen.get_size())
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
