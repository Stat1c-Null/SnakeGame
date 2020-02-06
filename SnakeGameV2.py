import pygame
import time
import random
pygame.init()

red = (255,0,0) 
white = (255,255,255)
black = (0,0,0)
gold = (212,175,55)

dis_height = 600
dis_width = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game by Nick")

snake_block = 10
snake_size = 25

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block)/10)*10
    foody = round(random.randrange(0, dis_width - snake_block)/10)*10t2

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("| Game Over | Q - Quit | P - Play Again |", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
                    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis,gold,[foodx,foody,snake_size,snake_size])
        pygame.draw.rect(dis,black,[x1,y1,snake_size,snake_size])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Test")
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
