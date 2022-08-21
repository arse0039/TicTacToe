import numpy as np
import pygame

WIDTH, HEIGHT = 600, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
GREY = (155, 155, 155)
BLACK = (0, 0, 0)
RED = (205, 45, 45)
FPS = 60
pygame.display.set_caption("Tic Tac Toe")
BOARD_ROWS = 3
BOARD_COLS = 3
game_board = np.zeros((BOARD_ROWS, BOARD_COLS))
WINNER = False


def draw_window():
    WINDOW.fill(GREY)
    for i in range(1, 3):
        pygame.draw.line(WINDOW, BLACK,  (200*i, 5), (200*i, 595), 5)
        pygame.draw.line(WINDOW, BLACK,  (5, 200 * i), (595, 200*i), 5)
    pygame.display.update()


def mark_spot(row, col, player):
    game_board[row][col] = player
    # return game_board[row][col]


def legal_move(row, col, player):
    if game_board[row][col] == 0:
        mark_spot(row, col, player)
        return True
    else:
        return False


def declare_winner(game_board, player):
    for i in range(3):
        if game_board[0][i] == game_board[1][i] and game_board[0][i] == game_board[2][i]:
            if game_board[0][i] != 0:
                draw_win_line(col=i)
                return True
        if game_board[i][0] == game_board[i][1] and game_board[i][0] == game_board[i][2]:
            if game_board[i][0] != 0:
                draw_win_line(row=i)
                return True
    if game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2]:
        if game_board[0][0] != 0:
            draw_win_line(diag1=1)
            return True
    if game_board[0][2] == game_board[1][1] and game_board[0][2] == game_board[2][0]:
        if game_board[0][2] != 0:
            draw_win_line(diag2=1)
            return True


def draw_circle(x_value, y_value, player):
    if legal_move(y_value, x_value, player):
        pygame.draw.circle(
            WINDOW, BLACK, (100 + 200*x_value, 100 + 200*y_value), 80)
        pygame.draw.circle(
            WINDOW, GREY, (100 + 200*x_value, 100 + 200*y_value), 65)
        pygame.display.update()


def draw_x(x_value, y_value, player):
    if legal_move(x_value, y_value, player):
        pygame.draw.line(WINDOW, BLACK, (15 + ((y_value)*200), 15 + (x_value*200)),
                         (185 + ((y_value)*200), 185 + ((x_value)*200)), 15)
        pygame.draw.line(WINDOW, BLACK, (15 + ((y_value)*200), 185 +
                                         ((x_value)*200)), (185 + ((y_value)*200), 15 + ((x_value)*200)), 15)
        pygame.display.update()


def draw_win_line(row=None, col=None, diag1=None, diag2=None):
    if row != None:
        pygame.draw.line(WINDOW, RED,  (5, 200*row+100),
                         (595, 200*row + 100), 15)
    elif col != None:
        pygame.draw.line(WINDOW, RED,  (100 + 200*col, 5),
                         (100 + 200*col, 595), 15)
    elif diag1 != None:
        pygame.draw.line(WINDOW, RED,  (5, 5), (595, 595), 11)
    elif diag2 != None:
        pygame.draw.line(WINDOW, RED, (595, 5), (5, 595), 11)
    pygame.display.update()


def game_restart():
    draw_window()
    for i in range(BOARD_ROWS):
        for k in range(BOARD_COLS):
            game_board[i][k] = 0


def main():
    clock = pygame.time.Clock()
    run = True
    player_turn = 1
    winner = False
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // 200
                row = event.pos[1] // 200
                if player_turn == 1 and winner == False:
                    draw_circle(col, row, 1)
                    if declare_winner(game_board, 1):
                        declare_winner(game_board, 1)
                        winner = True
                    player_turn = 2
                elif player_turn == 2 and winner == False:
                    draw_x(row, col, 2)
                    if declare_winner(game_board, 2):
                        declare_winner(game_board, 2)
                        winner = True
                    player_turn = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_turn = 1
                    winner = False
                    game_restart()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
