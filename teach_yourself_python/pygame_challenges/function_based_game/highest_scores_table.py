import pygame
import random
import sys
import os


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# -- Draw background
background_image = 'background.jpg'

def draw_background(screen, file_name):
    my_image = pygame.image.load(file_name)
    imagerect = my_image.get_rect()
    screen.blit(my_image, imagerect)

# Set player and enemy speed
PLAYER_SPEED = 5
ENEMY_SPEED = 5
BALL_SPEED = 5
BALL_SIZE = 10


# Define required score for winner
WINNING_SCORE = 100
# Limit of time
PLAYING_TIME = 30
# Import highscores file
HIGH_SCORES_FILE = "highscores.txt"


MENU_SCREEN = 0
GAME_SCREEN = 1
HIGH_SCORE_SCREEN = 2
SAVE_SCORE_SCREEN = 3


def draw_score(screen, x, y, score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score = " + str(score), 1, RED)
    screen.blit(text, (x, y))


def get_high_scores(file_name):
    content = ""
    if os.path.isfile(file_name):
        with open(file_name, "r") as content_file:
            content = content_file.read()
    else:
        f = open(file_name, "w")
        content = "high::0,mid::0,low::0"
        f.write(content)
        f.close()

    content_list = content.split(",")

    to_return = {}

    for ele in content_list:
        l = ele.split(":")
        to_return[l[0]] = [l[1], [l[2]]]
    
    return to_return


def write_high_scores(file_name, scores):
    f = open(file_name, "w")
    to_write = ""
    for name in ("high", "mid", "low"):
        to_write += name
        to_write += ":"
        to_write += str(scores.get(name)[0])
        to_write += ":"
        to_write += str(scores.get(name)[1])
        to_write += ","
    
    print(to_write)
    to_write = to_write[:-1]
    f.write(to_write)
    f.close()


def set_high_scores(file_name, player_name, score):
    scores = get_high_scores(file_name)     # get current high scores table

    if int(score) >= int(scores.get("high")[1]):
        scores["high"][0] = player_name
        scores["high"][1] = score
    elif int(score) <= int(scores.get("low")[1]):
        scores["low"][0] = player_name
        scores["low"][1] = score
    
    write_high_scores(file_name, scores)
    print(scores)


def draw_high_scores_table(screen, file_name):
    scores = get_high_scores(file_name)

    font = pygame.font.Font(None, 36)
    text = font.render("HIGH SCORES", 1, BLACK)
    screen.blit(text, (250, 100))
    
    font = pygame.font.Font(None, 30)
    text = font.render("1st: " + scores.get("high")[0] + " - " + scores.get("high")[1], 1, BLACK)
    screen.blit(text, (290, 200))

    text = font.render("2nd: " + scores.get("mid")[0] + " - " + scores.get("mid")[1], 1, BLACK)
    screen.blit(text, (290, 250))

    text = font.render("Lowest score: " + scores.get("low")[0] + " - " + scores.get("low")[1], 1, BLACK)
    screen.blit(text, (270, 300))

    text = font.render("Press E to return to the menu", 1, BLACK)
    screen.blit(text, (200, 400))


def draw_main_menu(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("WELCOME", 1, RED)
    screen.blit(text, (280, 100))

    font = pygame.font.Font(None, 30)
    text = font.render("1. P to Play", 1, BLACK)
    screen.blit(text, (290, 200))

    text = font.render("2. Q to Quit", 2, BLACK)
    screen.blit(text, (290, 250))

    text = font.render("3. S to Save", 1, BLACK)
    screen.blit(text, (290, 300))

    text = font.render("4. V to View High Scores", 1, BLACK)
    screen.blit(text, (230, 350))


def show_timer(screen, x, y, time_left):
    font = pygame.font.Font(None, 36)
    text = font.render("Time left = " + str(time_left), 1, WHITE)
    screen.blit(text, (x, y))


def draw_ball(screen, x, y):
    pygame.draw.circle(screen, (128, 0, 128), [x, y], BALL_SIZE, 0)


def show_game_over(screen, mess_1, mess_2):
    pygame.draw.rect(screen, WHITE, (150, 200, 400, 100), 0)

    font = pygame.font.Font(None, 36)
    text = font.render(mess_1, 1, RED)
    screen.blit(text, (160, 220))

    text = font.render(mess_2, 1, BLACK)
    screen.blit(text, (210, 260))

    font = pygame.font.Font(None, 28)
    text = font.render("Press P to play again. Press E to quit the game...", 1, WHITE)
    screen.blit(text, (100, 350))


# Define figure drawing function
def draw_stick_figure(screen, x, y, color, scale):
    pygame.draw.ellipse(screen, BLACK, [int(1 * scale) + x, y, int(10 * scale), int(10 * scale)], 0) 
    print(x,y)

    # Legs
    #Right leg (colour, length of leg....)
    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y], [int(10 * scale) + x, int(27 * scale) + y], int(2 * scale))
    #Left Leg
    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y], [x, int(27 * scale) + y], int(2 * scale))
 
    # Body
    pygame.draw.line(screen, color, [int(5 * scale) + x, int(17 * scale) + y], [int(5 * scale) + x, int(7 * scale) + y], int(2 * scale))
 
    # Arms
    pygame.draw.line(screen, color, [int(5 * scale) + x, int(7 * scale) + y], [int(9 * scale) + x, int(17 * scale) + y], int(2 * scale))
    pygame.draw.line(screen, color, [int(5 * scale) + x, int(7 * scale) + y], [int(1 * scale) + x, int(17 * scale) + y], int(2 * scale))

# Limit playing area
def keep_in_range(num, min_no, max_no):
    if num < min_no:
        return min_no
    if num > max_no:
        return max_no
    return num

# Setup
pygame.init()

# Set the width and height of the screen [width, height]
screen_size = [700, 500]
SCREEN = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Welcome to Gemma World")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()

# Counts the redrawn times of screem for every updates
step = 0

# Create a variable named score
score = 0

# Stores the step at which the last score was made
# Starts with a value of -100 so we can score on the first step of the game
last_score_step = -100

room = MENU_SCREEN
player_name = ""
high_score = 0

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 300
y_coord = 1

# Enemy's current position
enemy_x_coord = 200
enemy_y_coord = 200

# Enemy's last position
last_enemy_x_coord = 200
last_enemy_y_coord = 200

enemy_moves = (-ENEMY_SPEED, 0, ENEMY_SPEED)

# Store the current direction the enemy character is moving
enemy_x_dir = 0
enemy_y_dir = 0

# Ball current position
ball_x_coord = 300
ball_y_coord = 300

old_ball_x_coord = 300
old_ball_y_coord = 300

# Movement of ball
ball_moves = (-BALL_SPEED, BALL_SPEED)

ball_x_dir = 0
ball_y_dir = 0

done = False
game_over = False
game_end = False    # check if player ran out of time
while not done:
    for event in pygame.event.get():
        if room == MENU_SCREEN:

            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:  # Player pressed DOWN key
                if event.key == pygame.K_p:
                    room = GAME_SCREEN
                    score = 0
                    step = 0
                    last_score_step = 0
                    x_coord = 300
                    y_coord = 1

                    enemy_x_coord = 300
                    enemy_y_coord = 300

                    game_over = False
                    game_end = False

                    start_time = pygame.time.get_ticks()

                elif event.key == pygame.K_q:
                    done == True

                elif event.key == pygame.K_s:
                    room = SAVE_SCORE_SCREEN

                elif event.key == pygame.K_v:
                    room = HIGH_SCORE_SCREEN
        
        elif room == HIGH_SCORE_SCREEN:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    room == MENU_SCREEN
        
        elif room == SAVE_SCORE_SCREEN:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    player_name += chr(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    if len(player_name) > 1:
                        player_name = player_name[:-1]
                    else:
                        player_name = ""
                elif event.key == pygame.K_RETURN:
                    set_high_scores(HIGH_SCORES_FILE, player_name, high_score)
                    room = MENU_SCREEN
        
        elif room == GAME_SCREEN:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Player pressed LEFT key
                    x_speed = -PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:   # Player pressed RIGHT key
                    x_speed = PLAYER_SPEED
                elif event.key == pygame.K_UP:  # Player pressed UP key
                    y_speed = -PLAYER_SPEED
                elif event.key == pygame.K_DOWN:
                    y_speed = PLAYER_SPEED
                
                if game_over or game_end:
                    # if player presses p
                    if event.key == pygame.K_p:
                        score = 0
                        step = 0
                        last_score_step = 0
                        x_coord = 300
                        y_coord = 1

                        enemy_x_coord = 300
                        enemy_y_coord = 300

                        game_over = False
                        game_end = False

                        start_time = pygame.time.get_ticks() # reset the start time

                    # if player presses e
                    elif event.key == pygame.K_e:
                        room = MENU_SCREEN

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x_speed = 0
                elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                    y_speed = 0

    # Game logic
    if room == GAME_SCREEN:
        if start_time + PLAYING_TIME * 1000 <= pygame.time.get_ticks():
            game_end = True

        # Player moves according to the speed vector
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

        x_coord = max(x_coord, 0)
        y_coord = max(y_coord, 0)

        # Keep figure in frame
        x_coord = keep_in_range(x_coord, 5, screen_size[0] - 15) # maximum stick figures width
        y_coord = keep_in_range(y_coord, 0, screen_size[1] - 35) # maximum stick figures height

        # Enemy moves (setup automatically beforehand)
        # Every 30 steps, change the direction of enemy player
        if step % 30 == 0:
            enemy_x_dir = random.choice(enemy_moves)
            enemy_y_dir = random.choice(enemy_moves)

        # Update the old enemy coordinate value
        last_enemy_x_coord = enemy_x_coord
        last_enemy_y_coord = enemy_y_coord

        # Move the enemy player in the chosen direction
        enemy_x_coord = enemy_x_coord + enemy_x_dir
        enemy_y_coord = enemy_y_coord + enemy_y_dir

        # Keep enemy figure in frame
        enemy_x_coord = keep_in_range(enemy_x_coord, 0, screen_size[0] - 45)
        enemy_y_coord = keep_in_range(enemy_y_coord, 0, screen_size[1] - 105)

        # This step helps to make the movement of enemy player look more naturally
        if enemy_x_coord == last_enemy_x_coord:
            enemy_x_dir *= -1
        if enemy_y_coord == last_enemy_y_coord:
            enemy_y_dir *= -1

        # Move the ball
        if step % 50 == 0:
            ball_x_dir = random.choice(ball_moves)
            ball_y_dir = random.choice(ball_moves)

        # Update the old ball coord
        old_ball_x_coord = ball_x_coord
        old_ball_y_coord = ball_y_coord

        # Move the ball to designated position
        ball_x_coord += ball_x_dir
        ball_y_coord += ball_y_dir

        ball_x_coord = keep_in_range(ball_x_coord, 10, screen_size[0]-10)
        ball_y_coord = keep_in_range(ball_y_coord, 10, screen_size[1]-10)

        if ball_x_coord == old_ball_x_coord:
            ball_x_dir *= -1
        if (ball_y_coord == old_ball_y_coord):
            ball_y_dir *= -1

        # When player hits the ball, he gains score
        if ball_x_coord - BALL_SIZE <= x_coord + 5 and ball_x_coord + BALL_SIZE >= x_coord - 5 and ball_y_coord - BALL_SIZE <= y_coord + 27 and ball_y_coord + BALL_SIZE >= y_coord:
            if last_score_step + 10 < step:
                score += 10
                ball_x_dir *= -1
                ball_y_dir *= -1
                last_score_step = step # Record the step at which this score is made
                print(score)

        if x_coord - 5 <= enemy_x_coord + 10 and x_coord + 5 >= enemy_x_coord and y_coord - 3 <= enemy_y_coord + 54 and y_coord + 27 >= enemy_y_coord:
            print("COLLIDED WITH ENEMY")
            game_over = True

    # --- Drawing code

    SCREEN.fill((GREEN)) # Colorize background by yellow

    if room == MENU_SCREEN:
        draw_main_menu(SCREEN)
    elif room == HIGH_SCORE_SCREEN:
        draw_high_scores_table(SCREEN, HIGH_SCORES_FILE)
    elif room == SAVE_SCORE_SCREEN:
        set_high_scores(SCREEN, player_name, high_score)
    elif room == GAME_SCREEN:
        draw_background(SCREEN, background_image)

        if not game_over and not game_end:
            draw_stick_figure(SCREEN, x_coord, y_coord, RED, 1) #draw the user controlled stick figure on the screen
            draw_stick_figure(SCREEN, enemy_x_coord, enemy_y_coord, BLUE, 2) #draw the ai controlled stick figure on the screen

            draw_ball(SCREEN, ball_x_coord, ball_y_coord)

            draw_score(SCREEN, 550, 450, score)

            # Show time left on screen
            time_left = pygame.time.get_ticks() - start_time # calculate passed time
            time_left = time_left / 1000    # convert miliseconds into seconds
            time_left = int(PLAYING_TIME - time_left)   # true time left
            show_timer(SCREEN, 450, 50, time_left)

        elif game_over:
            show_game_over(SCREEN, "YOU LOSE, SORRY TRY AGAIN", "You hit the other player!")
        elif game_end:
            if score >= WINNING_SCORE:
                show_game_over(SCREEN, "YOU WIN THE GAME!", "Final Score: " + str(score))
            else:
                show_game_over(SCREEN, "YOU LOSE, SORRY TRY AGAIN", "You didn't score enough")


    pygame.display.flip()
    step += 1

    clock.tick(60)

pygame.quit()
