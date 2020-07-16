import pygame, sys
from pygame.locals import *

from typing import Tuple
from random import randint

BLACK = (0,0,0)
WHITE = (255,255,255)

class Ball(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    pygame.draw.rect(self.image, color, [0, 0, width, height])

    self.velocity = [randint(4, 8), randint(-8, 8)]
    self.rect = self.image.get_rect()

  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]

  def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

if __name__ == "__main__":
  pygame.display.init()
  pygame.display.set_caption("Game")

  screen = pygame.display.set_mode((700, 500))

  ball = Ball(WHITE, 10, 10)

  sprites = pygame.sprite.Group()
  sprites.add(ball)

  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False

    if ball.rect.x>690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    screen.fill(BLACK)
    
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)