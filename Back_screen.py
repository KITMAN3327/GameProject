import pygame
from Vsyakya import background_image_menu

pause_btns = list()


def back_btns(screen, size):
    width, height = 400, 120
    x = (size[0] - 400) / 2
    gap = (size[1] - 120 * 2) / 4
    from MAIN import Buttons
    for z in range(2):
        if z == 0:
            txt = "Resume"
            btn = Buttons(x, gap, width, height, screen, txt)
            btn.draw()
            pause_btns.append(btn)
        else:
            txt = "Back to Menu"
            btn = Buttons(x, height + 3 * gap, width, height, screen, txt)
            btn.draw()
            pause_btns.append(btn)


def run_back_screen(screen):
    screen.fill("black")
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    background_image_menu("PauseBack.jpg", size, screen)
    back_btns(screen, size)
    running = True
    while running:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
