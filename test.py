import numpy as np
import pygame

game_screen = pygame.display.set_mode((600, 600))
RED = (205, 45, 45)
GREY = (155, 155, 155)
test = np.zeros((3, 3))
test[1][0] = 1
test[1][1] = 1
test[1][2] = 1
test[2][0] = 2
test[2][1] = 2
test[2][2] = 2


def draw_window():
    game_screen.fill(GREY)
    pygame.display.update()


def draw_win_line(row=None, col=None, diag=None):
    if row != None:
        pygame.draw.line(game_screen, RED,  (5, 200*row+100),
                         (595, 200*row + 100), 5)
    elif col != False:
        pygame.draw.line(game_screen, RED,  (200*col, 5), (200*col, 595), 5)
    elif diag != False:
        pygame.draw.line(game_screen, RED,  (200*diag, 5), (200*diag, 595), 5)
    pygame.display.update()


def declare_winner(test):
    row_win = False
    col_win = False
    diag_win = False
    for i in range(3):
        if test[0][i] == test[1][i] and test[0][i] == test[2][i]:
            draw_win_line()
            return
        for k in range(3):
            pass


def main():
    game_state = True
    draw_window()
    while game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
            draw_win_line(row=1)
    pygame.quit()


# if a row [i] has all the same [k], you win
# if a col [i]
# main()

#print(1, 2, 3, end=" ")

for i in range(4):
    print(i, end=" ")
print('\n')
print(1, end=" ")
print(2)
