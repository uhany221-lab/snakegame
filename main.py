import pygame
import time
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# মোবাইল ফুলস্ক্রিনের জন্য অটো-ডিটেক্ট সাইজ
info = pygame.display.Info()
DIS_WIDTH = info.current_w if info.current_w > 0 else 800
DIS_HEIGHT = info.current_h if info.current_h > 0 else 480

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Termux Mobile Snake Game')

clock = pygame.time.Clock()
snake_block = 20  # মোবাইলের জন্য একটু বড় সাইজ
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 40)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    dis.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 8, DIS_HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = snake_block  # শুরুতে ডানদিকে যাবে
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / float(snake_block)) * snake_block
    foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / float(snake_block)) * snake_block

    while not game_over:

        while game_close == True:
            dis.fill(BLUE)
            message("You Lost! Tap Screen Top to Restart or Bottom to Quit", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if my < DIS_HEIGHT / 2:
                        gameLoop()
                    else:
                        game_over = True
                        game_close = False
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # মোবাইল স্ক্রিন টাচ কন্ট্রোল (স্ক্রিনের ৪টি দিক)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                else:
                    mx = event.x * DIS_WIDTH
                    my = event.y * DIS_HEIGHT

                # স্ক্রিনের ডান, বাম, উপর, নিচ হিসাব করে মুভমেন্ট
                if mx > DIS_WIDTH * 0.75 and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif mx < DIS_WIDTH * 0.25 and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif my < DIS_HEIGHT * 0.25 and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif my > DIS_HEIGHT * 0.75 and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, RED, [foodx, foody, snake_block, snake_block])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list=snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / float(snake_block)) * snake_block
            foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / float(snake_block)) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()
0

