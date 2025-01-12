from Vsyakya import *

platforms_rect = list()
platforms_tri = list()


def phantom(surface):
    pass


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
    def __init__(self, p1, p2, p3, k, height, scr):
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


def floor_rect(x, y, width, height, screen, move_screen):
    ground = Floor_rect(x, y, width, height, screen)
    ground.draw()
    pygame.draw.rect(move_screen, "red", (x, y, width, height))
    platforms_rect.append(ground)


def floor_tri(p1, p2, p3, k, height, screen, move_screen):
    ground = Floor_tri(p1, p2, p3, k, height, screen)
    ground.draw()
    pygame.draw.polygon(move_screen, "red", (p1, p2, p3))
    if k == 1 and height != 0:
        dot1 = min((p1, p2, p3), key=lambda x: (x[0], -x[1]))
        dot2 = min((p1, p2, p3), key=lambda x: (-x[0], -x[1]))
        pygame.draw.rect(move_screen, "red", (dot1[0], dot1[1], dot2[0] - dot1[0] + 2, height))
    platforms_tri.append(ground)


def game_run_1(screen):
    from MAIN import blackout
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    background_image_levels("Level_1.1_Back.jpg", size, screen)
    screen_for_move = pygame.Surface(size)
    screen_for_move.fill("black")
    floor_rect(0, size[1] * 7 / 10, size[0], size[1] * 3 / 10, screen, screen_for_move)
    # floor_rect(0, size[1] * (7 / 10), size[0] * (1 / 20), size[1] * (3 / 10), screen, screen_for_move)
    # floor_tri((size[0] * (1 / 20), size[1] * (7 / 10)), (size[0] * (1 / 20), size[1] * (8 / 10)),
    #           (size[0] * (2 / 20), size[1] * (8 / 10)), 1, size[1] * (2 / 10), screen, screen_for_move)
    # screen.blit(screen_for_move, (0, 0))
    paused = False
    while not paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    blackout(20, -1, screen, size)
        pygame.display.flip()
