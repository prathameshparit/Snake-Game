import pygame
import time
import random

#init game
pygame.init()

#define Colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
ORANGE = (255, 165, 0)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

width, height = 600,400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("PP's Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 80)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, WHITE)
    game_display.blit(text, [width/2-35, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, CYAN, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    #food
    target_x = round(random.randrange(0, width-snake_size)/ 10.0)* 10.0
    target_y = round(random.randrange(0, height-snake_size)/ 10.0)* 10.0

    while not game_over:

        while game_close:
            game_display.fill(BLACK)
            game_over_message = message_font.render("Game Over!", True, RED)
            game_display.blit(game_over_message, [width/3 -80, height / 3])
            print_score(snake_length -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_over = False
                    if event.key == pygame.K_RETURN:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_d:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_w:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_s:
                    x_speed = 0
                    y_speed = snake_size

        if x >=width or x < 0 or y >= height or y<0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(BLACK)
        pygame.draw.rect(game_display, GREEN, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append(([x,y]))

        if len(snake_pixels)> snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:  #snake ran into itself
                game_close = True
                pass

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()