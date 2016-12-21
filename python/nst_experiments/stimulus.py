# stimulus for EEG recording
import pygame
import sys
import time
from pygame.locals import *

pygame.init()

# setup the visualization parameters
WIDTH = 1680
HEIGHT = 1050
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()

# preparation time
win.fill(black)
time.sleep(10)

# experiment time
mins = 5
to_sec = 60

def main():

    t_end = time.time() + mins*to_sec
    while time.time() < t_end:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # epochs
        pygame.draw.rect(win, white, (0, 0, WIDTH/2, HEIGHT))
        pygame.display.update()
        time.sleep(8)
        win.fill(black)
        pygame.display.update()
        time.sleep(5)
        pygame.draw.rect(win, white, (WIDTH/2, 0, WIDTH/2, HEIGHT))
        pygame.display.update()
        time.sleep(8)
        win.fill(black)
        pygame.display.update()
        time.sleep(5)
        clock.tick(60)

main()