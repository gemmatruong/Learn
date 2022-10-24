import pygame
import random


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set player and enemy speed
PLAYER_SPEED = 5
ENEMY_SPEED = 5

# Define figure drawing function
def draw_stick_figure(screen, x, y, color, scale):
    # # Head
    # pygame.draw.circle(screen, BLACK, ((5 + x) * scale, (10 + y) * scale), 5 * scale)
    # print(x,y)

    # # Body
    # pygame.draw.line(screen, color, [(5 + x) * scale, (15 + y) * scale], [(5 + x) * scale, (25 + y) * scale], 2*scale)

    # # Legs
    # pygame.draw.line(screen, BLACK, [(5 + x) * scale, (25 + y) * scale], [(10 + x)*scale, (35 + y)*scale], 2*scale)
    # pygame.draw.line(screen, BLACK, [(5 + x) * scale, (25 + y) * scale], [x*scale, (35 + y)*scale], 2*scale)

    # # Arms
    # pygame.draw.line(screen, color, [(5 + x) * scale, (15 + y) * scale], [(9 + x)*scale, (20 + y)*scale], 2*scale)
    # pygame.draw.line(screen, color, [(5 + x) * scale, (15 + y) * scale], [(1 + x)*scale, (20 + y)*scale], 2*scale)

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

# Counts the redrawn times of screem for every updates
step = 0

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

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                x_speed = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                y_speed = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                y_speed = PLAYER_SPEED

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                x_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                y_speed = 0

    # Game logic
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


    # --- Drawing code

    # Whiten the screen
    SCREEN.fill(WHITE)

    draw_stick_figure(SCREEN, x_coord, y_coord, RED, 1) #draw the user controlled stick figure on the screen
    draw_stick_figure(SCREEN, enemy_x_coord, enemy_y_coord, BLUE, 2) #draw the ai controlled stick figure on the screen

    pygame.display.flip()
    step += 1

    clock.tick(50)

pygame.quit()
