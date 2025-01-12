import pygame
from Vsyakya import background_image_menu

pause_btns = list()


def back_btns(screen, size):
    from MAIN import Buttons
    width, height = 400, 120
    x = (size[0] - 400) / 2
    gap = (size[1] - 120 * 2) / 4
    for z in range(2):
        if z == 0:
            txt = "Resume"
            btn = Buttons(x, gap, width, height, screen, txt)
            btn.draw()
            pause_btns.append(btn)
        else:
            txt = "Back_to_levels_menu"
            btn = Buttons(x, height + 3 * gap, width, height, screen, txt)
            btn.draw()
            pause_btns.append(btn)


def run_back_screen(screen):
    from MAIN import blackout
    flag_back = 0
    flag = 0
    screen.fill("black")
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    background_image_menu("PauseBack.jpg", size, screen)
    back_btns(screen, size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                flag = 0
                x_pos, y_pos = pygame.mouse.get_pos()
                if (pause_btns[0].x <= x_pos <= (pause_btns[0].x + pause_btns[0].width) and
                        (pause_btns[0].y <= y_pos <= (pause_btns[0].y + pause_btns[0].height))):
                    running = False
                elif (pause_btns[-1].x <= x_pos <= (pause_btns[-1].x + pause_btns[-1].width) and
                      pause_btns[-1].y <= y_pos <= (pause_btns[-1].y + pause_btns[-1].height)):
                    running = False
                    flag_back = 1
                    flag = 1
                else:
                    for elem in pause_btns:
                        elem.draw()
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    for elem in pause_btns:
                        elem.change_col_mou()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = 1
                for elem in pause_btns:
                    elem.change_col_push()
        pygame.display.flip()
    if flag_back:
        blackout(5, 1, screen, size)
    else:
        blackout(20, 2, screen, size)
