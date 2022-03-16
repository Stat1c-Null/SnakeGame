import pygame as py
import random as r

#Colors     
snake_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
apple_color = (171, 38, 38)
background_color = (34, 179, 9)
score_color = (212, 208, 13)
speed_color = (144, 13, 209)
text_color = (128, 0, 255)
menu_color = (0, 0, 0)

#Set up display
py.init()
dis_width = 600
dis_height = 400
display = py.display.set_mode((dis_width, dis_height))
py.display.set_caption("Snake Game")
#Game Settings
clock = py.time.Clock()#Refresh the screen
fps = 15
snake_size = 20
#Food positions
x_pos = []
y_pos = []

font = py.font.SysFont("calibri", 20)
score_font = py.font.SysFont("comicsansms", 40)

def gameover_text(text):
  mesg = font.render(text, True, text_color)
  display.blit(mesg, [dis_width / 6, dis_height / 3])

def ui_text(score, speed):
  global score_color, speed_color
  mesg_score = score_font.render("Score: " + str(score), True, score_color)
  mesg_speed = score_font.render("Speed: " + str(speed), True, speed_color)
  display.blit(mesg_score, [10, 0])
  display.blit(mesg_speed, [440, 0])

def draw_snake(snake_list):
  global snake_size, snake_color
  for i in snake_list:
    py.draw.ellipse(display, snake_color, [i[0], i[1], snake_size, snake_size])

def spawn_food(num):
  global x_pos, y_pos
  #Generate positions
  for x in range(num):
    #Food position
    food_x = round(r.randrange(0 + snake_size, dis_width - snake_size) / 10) * 10
    x_pos.append(food_x)
    food_y = round(r.randrange(0 + snake_size, dis_height - snake_size) / 10) * 10
    y_pos.append(food_y)

def game_loop(restart: bool):
  global snake_color, food_color, snake_size, x_pos, y_pos
  game_over = False
  game_close = False
  game_start = restart
  #Player Position
  x1 = dis_width / 2 #Center of the screen
  y1 = dis_height / 2 #Current pos of the player
  collision_range = 15
  snake_speed = 10
  #update pos variables
  x1_change = 0
  y1_change = 0
  snake_list = []
  len_of_snake = 1
  speed_reset = 30
  num_apples = 5
  spawn_food(num_apples)#Generate positions

  while game_close == False:
    #Game Start Screen
    while game_start == False:
      display.fill(menu_color)
      gameover_text("Welcome to Snake Game! Press F to Start")
      py.display.update()#Keep stuff drawn on screen
      for event in py.event.get():
        if event.type == py.KEYDOWN:
          if event.key == py.K_f:
            game_start = True
          if event.key == py.K_q:
            game_close = True
            break
    #Game over but not closed
    while game_over == True:
      #Player lost the game, but still didnt close the game
      display.fill(menu_color)
      ui_text(len_of_snake - 1, snake_speed)
      gameover_text("You lost the game! Press R to Restart or Q to Quit!")
      py.display.update()
      for event in py.event.get():
        if event.type == py.KEYDOWN:
          if event.key == py.K_q:
            game_close = True
            game_over = False
            break
          elif event.key == py.K_r:
            game_loop(True)#Rerun the game
    for event in py.event.get():
      if event.type == py.QUIT:
        game_close = True
      #Controls
      if event.type == py.KEYDOWN:
        #WASD and Arrow Keys
        if event.key == py.K_a or event.key == py.K_LEFT:
          x1_change = -snake_speed
          y1_change = 0
        elif event.key == py.K_d or event.key == py.K_RIGHT:
          x1_change = snake_speed
          y1_change = 0
        elif event.key == py.K_w or event.key == py.K_UP:
          x1_change = 0
          y1_change = -snake_speed
        elif event.key == py.K_s or event.key == py.K_DOWN:
          x1_change = 0
          y1_change = snake_speed
    #Kill snake if it hits the wall
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
      game_over = True
    #Update snake position
    x1 += x1_change
    y1 += y1_change
    #Fill out background color
    display.fill(background_color)
    #Draw apple on the screen
    for i in range(num_apples):
      py.draw.ellipse(display, apple_color, [x_pos[i], y_pos[i], snake_size, snake_size])
    #draw snake on the screen
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    #Delete extra bodies of snake
    if len(snake_list) > len_of_snake:
      del snake_list[0]
    #Check if snake hit itself
    for x in snake_list[:-1]:
      if x == snake_head:
        game_over = True
    
    #Draw snake on the screen
    draw_snake(snake_list)
    #Draw score and speed on screen
    ui_text(len_of_snake - 1, snake_speed)
    #Update the screen
    py.display.update()
    #Check if snake picked up apple
    for z in range(num_apples):
      if (x1 <= x_pos[z] + collision_range and x1 >= x_pos[z] - collision_range) and (y1 <= y_pos[z] + collision_range and y1 >= y_pos[z] - collision_range):
        x_pos[z] = round(r.randrange(0 + snake_size, dis_width - snake_size) / 10) * 10
        y_pos[z] = round(r.randrange(0 + snake_size, dis_height - snake_size) / 10) * 10
        len_of_snake += 1
        snake_speed += 0.5
        #Reset speed 
        if snake_speed > speed_reset:
          snake_speed = 10
    clock.tick(fps)
  py.quit()
  quit()
#Start first time
game_loop(False)
