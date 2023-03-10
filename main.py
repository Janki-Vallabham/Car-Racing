import pygame
import time
import math

from pygame.constants import RESIZABLE
from utils import scale_image

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
FINISH = pygame.image.load("imgs/finish.png")

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

# WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((800,650))
pygame.display.set_caption("Racing Game!")

FPS = 60

class AbstractCar:
    # All of the stuff put over here can be used by both of player car and the computer car

    def __init__(self, max_vel, rotation_vel) -> None:
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0

    def rotate(self, left=False, right=False):
        if left:
            self.angle == self.rotation_vel
        elif right:
            self.angle == self.rotation_vel

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)

run = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)),(TRACK, (0,0))]

while run:
    clock.tick(FPS)

    draw(WIN, images)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
