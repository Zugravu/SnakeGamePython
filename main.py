import pygame
import random
import time

pygame.init()

DIMENSION = 32
X = 480
Y = 544

screen = pygame.display.set_mode((X, Y))

clock = pygame.time.Clock()
FPS = 60

running = True

# Board

first_tile = pygame.Surface([DIMENSION, DIMENSION])
first_tile.fill((9, 255, 0))
secound_tile = pygame.Surface([DIMENSION, DIMENSION])
secound_tile.fill((50, 220, 44))
score = 1
over_font = pygame.font.Font('freesansbold.ttf', 50)
font = pygame.font.Font('freesansbold.ttf', 32)


def draw_board():
    ok = "first_tile"
    for i in range(0, Y, DIMENSION):
        for j in range(0, X, DIMENSION):
            if j % DIMENSION == 0:
                if ok == "first_tile":
                    screen.blit(first_tile, (j, i))
                    ok = "secound_tile"
                else:
                    screen.blit(secound_tile, (j, i))
                    ok = "first_tile"
        if X / DIMENSION % 2 == 0:
            if ok == "first_tile":
                ok = "secound_tile"
            else:
                ok = "first_tile"


def game_over():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_board()
        game_over = over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(game_over, (90, 100))
        score_val = font.render("Score : " + str(score), True, (0, 0, 0))
        screen.blit(score_val, (170, 150))
        pygame.display.update()


# Snake
snakeHead = pygame.Surface([DIMENSION, DIMENSION])
snakeHead.fill((0, 0, 0))
snake = [score]
snakeX = [64]
snakeY = [256]
snakeX_change = 0
snakeY_change = 0


def snake_draw(x, y):
    for i in range(len(snake)):
        screen.blit(snakeHead, (x[i], y[i]))


# Snack
snackImg = pygame.Surface([DIMENSION, DIMENSION])
snackImg.fill((255, 0, 0))
snackX = random.randrange(0, X - DIMENSION, DIMENSION)
snackY = random.randrange(0, Y - DIMENSION, DIMENSION)
snackX_change = snackX
snackY_change = snackY


def snack_draw(x, y):
    screen.blit(snackImg, (x, y))






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snakeY_change != 32:
                    snakeY_change = -32
                    snakeX_change = 0
            if event.key == pygame.K_DOWN:
                if snakeY_change != -32:
                    snakeY_change = 32
                    snakeX_change = 0
            if event.key == pygame.K_RIGHT:
                if snakeX_change != -32:
                    snakeY_change = 0
                    snakeX_change = 32
            if event.key == pygame.K_LEFT:
                if snakeX_change != 32:
                    snakeY_change = 0
                    snakeX_change = -32

    if snakeX[0] == snackX and snakeY[0] == snackY:  # Eat snack
        score += 1
        snackX_change = random.randrange(0, X - DIMENSION, DIMENSION)
        snackY_change = random.randrange(0, Y - DIMENSION, DIMENSION)
        for i in range(0, len(snake)):
            if snackX_change == snakeX[i] and snackY_change == snakeY[i]:
                i = 0
                snackX_change = random.randrange(0, X - DIMENSION, DIMENSION)
                snackY_change = random.randrange(0, Y - DIMENSION, DIMENSION)

        snake.append(score)
        snakeX.append(0)
        snakeY.append(0)

    if snakeX[0] < 0 or snakeX[0] > X or snakeY[0] < 0 or snakeY[0] > Y:  # Border
        snakeX = 1000
        snackX = -1000
        game_over()
        running = False
        break

    for i in range(1, len(snake)):  # Tail border
        if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
            game_over()
            running = False
            break

    time.sleep(0.09)
    draw_board()

    snackX = snackX_change
    snackY = snackY_change
    snack_draw(snackX, snackY)

    for i in range(len(snake) - 1, 0, -1):
        snakeX[i] = snakeX[i - 1]
        snakeY[i] = snakeY[i - 1]

    snakeX[0] += snakeX_change
    snakeY[0] += snakeY_change
    snake_draw(snakeX, snakeY)

    clock.tick(FPS)
    pygame.display.update()

