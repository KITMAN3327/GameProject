from Vsyakya import *
from Level_1 import game_run_1
from Back_screen import run_back_screen

main_btns = list()
levels_btns = list()


def running_mw(screen, size):
    flag_exit = 0
    flag = 0
    background_image_menu("MainBack.jpg", size, screen)
    srart_btns(screen, size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                flag = 0
                x_pos, y_pos = pygame.mouse.get_pos()
                if (main_btns[0].x <= x_pos <= (main_btns[0].x + main_btns[0].width) and
                        (main_btns[0].y <= y_pos <= (main_btns[0].y + main_btns[0].height))):
                    running = False
                elif (main_btns[-1].x <= x_pos <= (main_btns[-1].x + main_btns[-1].width) and
                      main_btns[-1].y <= y_pos <= (main_btns[-1].y + main_btns[-1].height)):
                    running = False
                    flag_exit = 1
                    flag = 1
                else:
                    for elem in main_btns:
                        elem.draw()
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    for elem in main_btns:
                        elem.change_col_mou()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = 1
                for elem in main_btns:
                    elem.change_col_push()
        pygame.display.flip()
    if flag_exit:
        pygame.quit()
    else:
        blackout(5, 1, screen, size)


def running_sw(screen, size):
    lvl_switch = 0
    flag = 0
    background_image_menu("StartBack.jpg", size, screen)
    lvls_btns(screen, size)
    lvls_back_btn(screen, size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                flag = 0
                x_pos, y_pos = pygame.mouse.get_pos()
                if (levels_btns[0].x <= x_pos <= (levels_btns[0].x + levels_btns[0].width) and
                        levels_btns[0].y <= y_pos <= (levels_btns[0].y + levels_btns[0].height)):
                    running = False
                    lvl_switch = 1
                elif (levels_btns[-1].x <= x_pos <= (levels_btns[-1].x + levels_btns[-1].width) and
                      levels_btns[-1].y <= y_pos <= (levels_btns[-1].y + levels_btns[-1].height)):
                    running = False
                else:
                    for elem in levels_btns:
                        elem.draw()
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    for elem in levels_btns:
                        elem.change_col_mou()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = 1
                for elem in levels_btns:
                    elem.change_col_push()
        pygame.display.flip()
    if lvl_switch == 0:
        blackout(5, 0, screen, size)
    elif lvl_switch == 1:
        blackout(5, 2, screen, size)


def blackout(fade_speed, k, screen, size):
    kirkorov = [screen.get_at((x, size[1] // 2)) for x in range(size[0])]
    alpha = 0
    overlay = pygame.Surface(size)
    while any(is_black(x) for x in kirkorov):
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        if alpha < 255:
            alpha += fade_speed
        pygame.display.flip()
        pygame.time.delay(30)
        kirkorov = [screen.get_at((x, size[1] // 2)) for x in range(size[0])]
    if k == 0:
        running_mw(screen, size)
    elif k == 1:
        running_sw(screen, size)
    elif k == 2:
        game_run_1(screen)
    elif k == -1:
        run_back_screen(screen)


def is_black(dot):
    if dot == (0, 0, 0):
        return False
    return True


def srart_btns(screen, size):
    width, height = 300, 100
    x = (size[0] - 300) / 2
    gap = (size[1] - 100 * 3) / 6
    for z in range(3):
        if z == 0:
            txt = "Start"
        elif z == 1:
            txt = "Settings"
        else:
            txt = "Exit"
        btn = Buttons(x, (z + 2) * gap + z * height, width, height, screen, txt)
        btn.draw()
        main_btns.append(btn)


def lvls_btns(screen, size):
    k = 0
    for y in range(2):
        for x in range(5):
            k += 1
            width, height = 150, 100
            gap_x = (size[0] - width * 5) / 8
            gap_y = (size[1] - height * 3 - 75) / 5
            if k != 1:
                txt = "Locked"
            else:
                txt = str(k)
            btn = Buttons((x + 2) * gap_x + x * width, (y + 2) * gap_y + y * height - 70, width, height, screen, txt)
            btn.draw()
            levels_btns.append(btn)


def lvls_back_btn(screen, size):
    width, height = 450, 100
    btn = Buttons((size[0] - width) / 2, size[1] - 200, width, height, screen, "Back")
    btn.draw()
    levels_btns.append(btn)


class Buttons:
    def __init__(self, x, y, width, height, scr, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = scr
        self.col = (38, 166, 147)
        self.text = text
        self.font = pygame.font.Font(None, 32)

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 50, self.col[2]),
                         (self.x, self.y, self.width, self.height), 7)
        text = self.font.render(self.text, True, "black")
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.scr.blit(text, text_rect)

    def change_col_mou(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        if self.x <= x_pos <= self.x + self.width and self.y <= y_pos <= self.y + self.height:
            pygame.draw.rect(self.scr, (self.col[0], self.col[1] + 30, self.col[2]),
                             (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 20, self.col[2]),
                             (self.x, self.y, self.width, self.height), 7)
            text = self.font.render(self.text, True, "black")
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            self.scr.blit(text, text_rect)
        else:
            self.draw()

    def change_col_push(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        if self.x <= x_pos <= self.x + self.width and self.y <= y_pos <= self.y + self.height:
            pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 30, self.col[2]),
                             (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 80, self.col[2]),
                             (self.x, self.y, self.width, self.height), 7)
            text = self.font.render(self.text, True, "black")
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            self.scr.blit(text, text_rect)


if __name__ == "__main__":
    pygame.init()
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size)
    running_mw(screen, size)
