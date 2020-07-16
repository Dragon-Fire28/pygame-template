import pygame, sys
from pygame.locals import *

if __name__ == "__main__":
  pygame.display.init()
  pygame.display.set_caption("Game")

  screen = pygame.display.set_mode((240, 180))

  screen.fill((255, 0, 0))
  pygame.display.flip()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False