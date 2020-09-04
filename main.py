import pygame as pg
import math
import sys
import verification as ver
import time

# Fonts
pg.font.init()
X_O_FONT = pg.font.SysFont('comicsans', 65)
Draw_FONT = pg.font.SysFont('comicsans', 70)
WORD_FONT = pg.font.SysFont('comicsans', 30)
# Colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
# Display settings
FPS = 60
SQUARE = 240
win = pg.display.set_mode([SQUARE, SQUARE])
clock = pg.time.Clock()
pg.init()
# Buttons
buttons = []
for i in range(1, 10):
    pos = i
    state = ""
    buttons.append([pos, state, False])
# Tiles
tiles = []
for i in range(1, 10):
    pos = i
    state = ""
    tiles.append([pos, state])


def draw_game(buttons):
    for i in range(1, 3):
        pg.draw.line(win, BLACK, [80 * i, 0], [80 * i, 240], 1)
    for j in range(1, 3):
        pg.draw.line(win, BLACK, [0, 80 * j], [240, 80 * j], 1)
    for button in buttons:
        text = X_O_FONT.render('{}'.format(button[1]), 1, BLACK)
        if button[0] <= 3:
            win.blit(text, [40 + 80 * (button[0] - 1) - text.get_width() / 2, 40 - text.get_width() / 2])
        if 3 < button[0] <= 6:
            if 3 < button[0] < 6:
                win.blit(text, [40 + 80 * (button[0] // 5) - text.get_width() / 2, 120 - text.get_width() / 2])
            if button[0] == 6:
                win.blit(text, [40 + 80 * (button[0] // 3) - text.get_width() / 2, 120 - text.get_width() / 2])
        if 6 < button[0] <= 9:
            if 6 < button[0] < 9:
                win.blit(text, [40 + 80 * (button[0] // 8) - text.get_width() / 2, 200 - text.get_width() / 2])
            if button[0] == 9:
                win.blit(text, [40 + 80 * (button[0] // 4) - text.get_width() / 2, 200 - text.get_width() / 2])


def draw_win(result, win):
    win.fill(WHITE)
    if result == "Player X has won":
        text = WORD_FONT.render(result, 1, BLACK)
        win.blit(text, [SQUARE / 2 - text.get_width() / 2, SQUARE / 2 - text.get_height() / 2])
        pg.display.flip()
        time.sleep(1)
        sys.exit()
    if result == "Player O has won":
        text = WORD_FONT.render(result, 1, BLACK)
        win.blit(text, [SQUARE / 2 - text.get_width() / 2, SQUARE / 2 - text.get_height() / 2])
        pg.display.flip()
        time.sleep(1)
        sys.exit()
    else:
        text = Draw_FONT.render("Draw", 1, BLACK)
        win.blit(text, [SQUARE / 2 - text.get_width() / 2, SQUARE / 2 - text.get_height() / 2])
        pg.display.flip()
        time.sleep(1)
        sys.exit()


turn = 0
while True:
    clock.tick(FPS)
    win.fill(WHITE)
    events = pg.event.get()
    draw_game(buttons)

    for event in events:
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            m_x, m_y = pg.mouse.get_pos()
            button, selection, turn = ver.modify_state(buttons, m_x, m_y, turn)
            buttons[selection - 1] = button
    result = ver.verify_win_condition(buttons)
    if result is not 0 or turn is 9:
        draw_game(buttons)
        pg.display.flip()
        time.sleep(0.5)
        draw_win(result, win)
    pg.display.flip()
