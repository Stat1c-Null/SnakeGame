import pygame as py
import random as r

snake_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
food_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
background_color = (30, 30, 30)
score_color = (0, 255, 64)
game_over_colors = (0, 47, 255)
background_game_over = (0, 0, 0)
speed_color = (255, 10, 10)

py.init()
dis_width = 800
dis_height = 600
display = py.display.set_mode((dis_width, dis_height))
py.display.set_caption("Snake Game")

clock = py.time.Clock()
snake_size = 20
snake_speed = 10
font = py.font.SysFont("calibri", 20)
score_font = py.font.SysFont("calibri", 40)

def screen_text(msg):
  message = font.render(msg, True, game_over_colors)
  display.blit(message, [dis_width / 4, dis_height / 3])


def score_text(score):
  global snake_speed, speed_color
  message_score = score_font.render("Score: " + str(score), True, score_color)
  message_speed = score_font.render("Speed: " + str(snake_speed), True, speed_color)
  display.blit(message_score, [0, 0])
  display.blit(message_speed, [150, 0])


def snake(snake_list):
  global snake_size
  #snake_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
  for i in snake_list:
    py.draw.ellipse(display, snake_color, [i[0], i[1], snake_size, snake_size])


def game_loop():
  global snake_color,food_color,snake_speed
  game_over = False
  game_close = False
  game_start = False
  phrase = "LMAO NOOB!!!!!!!!!!!!!!!!"
  #players position
  x1 = dis_width / 2  #Current position of the player
  y1 = dis_height / 2
  collision_range = 15
  x1_change = 0  #Update x axis
  y1_change = 0
  snake_list = []
  length_of_snake = 1
  food_x = round(r.randrange(0, dis_width - snake_size) / 10) * 10
  food_y = round(r.randrange(0, dis_height - snake_size) / 10) * 10
  food_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
  while not game_close == True:
    while game_start == False:
      display.fill(background_game_over)
      screen_text("Welcome to Snake Game! Press F to Start!")
      py.display.update()
      for event in py.event.get():
        if event.type == py.KEYDOWN:
          if event.key == py.K_f:
            game_start = True
    # game over screen
    while game_over == True :
      display.fill(background_game_over)
      screen_text(phrase)
      score_text(length_of_snake-1)
      py.display.update()
      for event in py.event.get():
        if event.type == py.KEYDOWN:
          if event.key == py.K_q:
            game_close = True
            game_over = False
            break
          elif event.key == py.K_r:
            game_loop()
    for event in py.event.get():
      if event.type == py.QUIT:
        game_close = True 
      #controls
      if event.type == py.KEYDOWN:
        #WASD
        if event.key == py.K_a:
          x1_change = -snake_speed
          y1_change = 0
        elif event.key == py.K_d:
          x1_change = snake_speed
          y1_change = 0
        elif event.key == py.K_w:
          x1_change = 0
          y1_change = -snake_speed
        elif event.key == py.K_s:
          x1_change = 0
          y1_change = snake_speed
        #ARROW KEYS
        if event.key == py.K_LEFT:
          x1_change = -snake_speed
          y1_change = 0
        elif event.key == py.K_RIGHT:
          x1_change = snake_speed
          y1_change = 0
        elif event.key == py.K_UP:
          x1_change = 0
          y1_change = -snake_speed
        elif event.key == py.K_DOWN:
          x1_change = 0
          y1_change = snake_speed
    # kill snake if it touches wall
    if x1 >= dis_width or x1 <0 or y1 >= dis_height or y1 <0 :
      phrase = "Watch out for walls buddy. Press R to Restart and Q to Quit"
      game_over = True
    #add changed postion to players current position
    x1 += x1_change
    y1 += y1_change
    # fill background with background_color
    display.fill(background_color)
    # draw food on screen
    py.draw.ellipse(display,food_color,[food_x, food_y,snake_size,snake_size])
    #draw snake on screen
    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    #Delete extra pieces of snake body 
    if len(snake_list) > length_of_snake:
      del snake_list[0]
    #kill snake if it eats itself
    for x in snake_list[:-1]:
      if x == snake_head :
        phrase = "Don't eat yourself! Press R to Restart, Q to Quit."
        game_over = True
    snake(snake_list)
    # show score in the game
    score_text(length_of_snake-1)
    py.display.update()
    #check if snake picked up food
    if(x1 <= food_x +collision_range and x1 >= food_x -collision_range) and (y1 <= food_y +collision_range and y1 >= food_y -collision_range):
      food_x = round(r.randrange(0, dis_width - snake_size) / 10) * 10
      food_y = round(r.randrange(0, dis_height - snake_size) / 10) * 10
      length_of_snake +=1
      snake_speed +=0.5
      snake_color = food_color #change snake into color of joe
      food_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    clock.tick(15)
  py.quit()
  quit()
game_loop()