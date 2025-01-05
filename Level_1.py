import pygame
from Vsyakya import background_image_levels

platforms = list()


class Floor:
    def __init__(self, x, y, width, height, scr):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = scr
        self.col = (215, 105, 10)

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (15, 130, 30), (self.x, self.y, self.width, 10))


def floor(size, screen):
    ground = Floor(0, size[1] - size[1] * (1 / 10), size[0] * (2 / 10), size[1] * (1 / 10), screen)
    ground.draw()
    platforms.append(ground)


def game_run_1(screen):
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen.fill("black")
    background_image_levels("Level_1.1_Back.jpg", size, screen)
    floor(size, screen)
    paused = False
    while not paused:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
