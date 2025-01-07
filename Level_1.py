import pygame
from Vsyakya import background_image_levels
from MAIN import Buttons

platforms_rect = list()
platforms_tri = list()


class Floor_rect:
    def __init__(self, x, y, width, height, scr):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = scr
        self.col = (215, 105, 10)
        self.earth = (15, 130, 30)

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, self.earth, (self.x, self.y, self.width, 10))


class Floor_tri:
    def __init__(self, p1, p2, p3, scr, k, height):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.scr = scr
        self.k = k
        self.height = height
        self.col = (215, 105, 10)
        self.earth = (15, 130, 30)

    def draw(self):
        pygame.draw.polygon(self.scr, self.col, (self.p1, self.p2, self.p3))
        if self.k == 1 and self.height != 0:
            dot1 = min((self.p1, self.p2, self.p3), key=lambda x: (x[0], -x[1]))
            dot2 = min((self.p1, self.p2, self.p3), key=lambda x: (-x[0], -x[1]))
            pygame.draw.rect(self.scr, self.col, (dot1[0], dot1[1], dot2[0] - dot1[0], self.height))
        pygame.draw.polygon(self.scr, self.earth,
                            (self.p1, (self.p1[0], self.p1[1] + 10), (self.p3[0], self.p3[1] + 10), self.p3))


def floor_rect(x, y, width, height, screen):
    ground = Floor_rect(x, y, width, height, screen)
    ground.draw()
    platforms_rect.append(ground)


def floor_tri(p1, p2, p3, screen, k, height):
    ground = Floor_tri(p1, p2, p3, screen, k, height)
    ground.draw()
    platforms_tri.append(ground)


def game_run_1(screen):
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen.fill("black")
    background_image_levels("Level_1.1_Back.jpg", size, screen)
    floor_rect(0, size[1] * (7 / 10), size[0] * (1 / 20), size[1] * (3 / 10), screen)
    floor_tri((size[0] * (1 / 20), size[1] * (7 / 10)), (size[0] * (1 / 20), size[1] * (8 / 10)),
              (size[0] * (2 / 20), size[1] * (8 / 10)), screen, 1, size[1] * (2 / 10))
    paused = False
    while not paused:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
