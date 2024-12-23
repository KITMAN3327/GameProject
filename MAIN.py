import pygame

btns = list()


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


def srart_btns():
    width, height = 500, 200
    x = (size.current_w - 500) / 2
    gap = (size.current_h - 200 * 3) / 6
    for z in range(3):
        if z == 0:
            btn = Buttons(x, 2 * gap, width, height, screen, (0, 200, 0), "Start")
            btn.draw()
            btn.txt()
            btns.append(btn)
        elif z == 1:
            btn = Buttons(x, 3 * gap + height, width, height, screen, (0, 200, 0), "Settings")
            btn.draw()
            btn.txt()
            btns.append(btn)
        else:
            btn = Buttons(x, 4 * gap + 2 * height, width, height, screen, (0, 200, 0), "Exit")
            btn.draw()
            btn.txt()
            btns.append(btn)


def exit(x_pos, y_pos):
    global running
    if btns[2].x <= x_pos <= btns[2].x + btns[2].width:
        if btns[2].y <= y_pos <= (btns[2].y + btns[2].height):
            running = False


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.Font(None, 36)
    size = pygame.display.Info()
    screen = pygame.display.set_mode((size.current_w, size.current_h))
    srart_btns()
    for x in btns:
        print(x.__dict__)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                exit(x, y)
        pygame.display.flip()
    pygame.display.flip()
    pygame.quit()
