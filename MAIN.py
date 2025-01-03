import pygame

main_btns = list()
levels_btns = list()


def running_mw():
    flag_exit = 0
    flag = 0
    screen.fill("black")
    background_image("MainBack.jpg", size)
    srart_btns()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                flag = 0
                x_pos, y_pos = pygame.mouse.get_pos()
                if main_btns[0].x <= x_pos <= (main_btns[0].x + main_btns[0].width):
                    if main_btns[0].y <= y_pos <= (main_btns[0].y + main_btns[0].height):
                        running = False
                    if main_btns[-1].y <= y_pos <= (main_btns[-1].y + main_btns[-1].height):
                        running = False
                        flag_exit = 1
                        flag = 1
                else:
                    for elem in main_btns:
                        elem.draw()
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    x_pos, y_pos = pygame.mouse.get_pos()
                    for elem in main_btns:
                        if elem.x <= x_pos <= elem.x + elem.width and elem.y <= y_pos <= elem.y + elem.height:
                            elem.change_col_mou()
                        else:
                            elem.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = 1
                x_pos, y_pos = pygame.mouse.get_pos()
                for elem in main_btns:
                    if elem.x <= x_pos <= elem.x + elem.width and elem.y <= y_pos <= elem.y + elem.height:
                        elem.change_col_push()
        pygame.display.flip()
    if flag_exit == 1:
        pygame.quit()
    else:
        running_sw()


def running_sw():
    flag = 0
    screen.fill("black")
    background_image("StartBack.jpg", size)
    lvls_btns()
    lvls_back_btn()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                flag = 0
                x_pos, y_pos = pygame.mouse.get_pos()
                if levels_btns[-1].x <= x_pos <= (levels_btns[-1].x + levels_btns[-1].width):
                    if levels_btns[-1].y <= y_pos <= (levels_btns[-1].y + levels_btns[-1].height):
                        running = False
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    x_pos, y_pos = pygame.mouse.get_pos()
                    for elem in levels_btns:
                        if elem.x <= x_pos <= elem.x + elem.width and elem.y <= y_pos <= elem.y + elem.height:
                            elem.change_col_mou()
                        else:
                            elem.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = 1
                x_pos, y_pos = pygame.mouse.get_pos()
                for elem in levels_btns:
                    if elem.x <= x_pos <= elem.x + elem.width and elem.y <= y_pos <= elem.y + elem.height:
                        elem.change_col_push()
        pygame.display.flip()
    running_mw()


def srart_btns():
    width, height = 300, 100
    x = (size[0] - 300) / 2
    gap = (size[1] - 100 * 3) / 6
    for z in range(3):
        txt = ""
        if z == 0:
            txt = "Start"
        elif z == 1:
            txt = "Settings"
        else:
            txt = "Exit"
        btn = Buttons(x, (z + 2) * gap + z * height, width, height, screen, txt)
        btn.draw()
        main_btns.append(btn)


def lvls_btns():
    k = 0
    for y in range(2):
        for x in range(5):
            k += 1
            width, height = 150, 100
            gap_x = (size[0] - width * 5) / 8
            gap_y = (size[1] - height * 3 - 75) / 5
            btn = Buttons((x + 2) * gap_x + x * width, (y + 2) * gap_y + y * height - 70, width, height, screen, str(k))
            btn.draw()
            levels_btns.append(btn)


def lvls_back_btn():
    width, height = 450, 100
    btn = Buttons((size[0] - width) / 2, size[1] - 200, width, height, screen, "Back")
    btn.draw()
    levels_btns.append(btn)


def background_image(name, size):
    image = pygame.image.load(f"Backgrounds/{name}")
    image = pygame.transform.scale(image, size)
    screen.blit(image, (0, 0))


class Buttons:
    def __init__(self, x, y, width, height, scr, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scr = scr
        self.col = (38, 166, 147)
        self.text = text

    def draw(self):
        pygame.draw.rect(self.scr, self.col, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 50, self.col[2]),
                         (self.x, self.y, self.width, self.height), 7)
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.scr.blit(text, text_rect)

    def change_col_mou(self):
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] + 30, self.col[2]),
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 20, self.col[2]),
                         (self.x, self.y, self.width, self.height), 7)
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.scr.blit(text, text_rect)

    def change_col_push(self):
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 30, self.col[2]),
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.scr, (self.col[0], self.col[1] - 80, self.col[2]),
                         (self.x, self.y, self.width, self.height), 7)
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.scr.blit(text, text_rect)


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.Font(None, 32)
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size)
    running_mw()
