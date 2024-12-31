import pygame

Main_btns = list()
levels_buttons = list()


def running_mw():
    flag = 0
    screen.fill("black")
    srart_btns()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                if Main_btns[0].x <= x_pos <= (Main_btns[0].x + Main_btns[0].width):
                    if Main_btns[0].y <= y_pos <= (Main_btns[0].y + Main_btns[0].height):
                        running = False
                if Main_btns[-1].x <= x_pos <= (Main_btns[-1].x + Main_btns[-1].width):
                    if Main_btns[-1].y <= y_pos <= (Main_btns[-1].y + Main_btns[-1].height):
                        running = False
                        flag = 1
            pygame.display.flip()
    if flag == 1:
        pygame.quit()
    else:
        running_sw()


def running_sw():
    screen.fill("black")
    lvls_btns()
    lvls_back_btn()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                if levels_buttons[-1].x <= x_pos <= (levels_buttons[-1].x + levels_buttons[-1].width):
                    if levels_buttons[-1].y <= y_pos <= (levels_buttons[-1].y + levels_buttons[-1].height):
                        running = False
        pygame.display.flip()
    running_mw()


def srart_btns():
    width, height = 500, 200
    x = (size.current_w - 500) / 2
    gap = (size.current_h - 200 * 3) / 6
    for z in range(3):
        txt = ""
        if z == 0:
            txt = "Start"
        elif z == 1:
            txt = "Settings"
        else:
            txt = "Exit"
        btn = Buttons(x, (z + 2) * gap + z * height, width, height, screen, (0, 200, 0), txt)
        btn.draw()
        btn.txt()
        Main_btns.append(btn)


def lvls_btns():
    screen.fill("black")
    k = 0
    for y in range(3):
        for x in range(5):
            k += 1
            width, height = 200, 150
            gap_x = (size.current_w - width * 5) / 8
            gap_y = (size.current_h - height * 3 - 150) / 6
            btn = Buttons((x + 2) * gap_x + x * width, (y + 2) * gap_y + y * height, width, height, screen,
                          (0, 200, 0),
                          str(k))
            btn.draw()
            btn.txt()
            levels_buttons.append(btn)


def lvls_back_btn():
    width, height = 600, 150
    btn = Buttons((size.current_w - width) / 2, size.current_h - 200, width, height, screen, (0, 200, 0),
                  "Back")
    btn.draw()
    btn.txt()
    levels_buttons.append(btn)


class Buttons:
    def __init__(self, x, y, width, height, scr, col, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = scr
        self.col = col
        self.text = text

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 100, self.col[2]),
                         (self.x, self.y, self.width, self.height), 7)

    def txt(self):
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.scr.blit(text, text_rect)


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.Font(None, 52)
    size = pygame.display.Info()
    screen = pygame.display.set_mode((size.current_w, size.current_h))
    running_mw()
