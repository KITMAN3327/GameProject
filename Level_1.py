import pygame
from Vsyakya import background_image_levels

platforms = list()


class Floor:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = screen
        self.col = (215, 105, 10)

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 50, self.col[1]), (self.x, self.y, self.width, 10))


def floor():
    ground = Floor(0, size[1] - size[1] * (1 / 10), size[0] * (2 / 10), size[1] * (1 / 10))
    ground.draw()
    platforms.append(ground)


def game_run_1():
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size)
    screen.fill("black")
    background_image_levels("Level_1.1_Back.jpg", size, screen)
    floor()
    paused = False
    while not paused:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
