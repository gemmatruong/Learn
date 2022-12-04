import pygame
import random
import math
import sys
import os


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class PlayerBall(Ball):
    def __init__(self, x, y, radius, color, screen):
        super().__init__(x, y, radius, color, screen)
        self.enemy_cooldown = 0
        self.health_cooldown = 0

    def move(self, mv_type):
        if mv_type == "UP":
            self.y -= 5
        elif mv_type == "DOWN":
            self.y += 5
        elif mv_type == "LEFT":
            self.x -= 5
        elif mv_type == "RIGHT":
            self.x += 5

        # Keep the ball in frame
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.y - self.radius <= 0:
            self.y = self.radius
        elif self.x + self.radius >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
        elif self.y + self.radius >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius

    def collision_check(self, health, enemy):
        to_return = 0
        # Check collision with enemy ball
        if math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2) < self.radius + enemy.radius:
            if self.enemy_cooldown == 0:
                self.enemy_cooldown = 10
                to_return -= 10
        # Check collision with health ball
        if math.sqrt((self.x - health.x)**2 + (self.y - health.y)**2) < self.radius + health.radius:
            if self.health_cooldown == 0:
                self.health_cooldown = 10
                to_return += 10
        return to_return


class HealthBall(Ball):
    def __init__(self, x, y, radius, color, screen):
        super().__init__(x, y, radius, color, screen)
        self.vx = random.randint(0, 4) - 2
        self.vy = random.randint(0, 4) - 2

        while self.vx == 0 or self.vy == 0:
            self.vx = random.randint(0, 4) - 2
            self.vy = random.randint(0, 4) - 2


    def move(self):
        self.x += self.vx
        self.y += self.vy

        # If health ball move to outside the frame, multiply velocity to -1 to change direction
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1
        elif self.y - self.radius <= 0:
            self.y = self.radius
            self.vy *= -1
        elif self.x + self.radius >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vx *= -1
        elif self.y + self.radius >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.vy *= -1


class EnemyBall(Ball):
    def __init__(self, x, y, radius, color, screen):
        super().__init__(x, y, radius, color, screen)
        self.vx = random.randint(0, 6) - 3
        self.vy = random.randint(0, 6) - 3

        while self.vx == 0 or self.vy == 0:
            self.vx = random.randint(0, 6) - 3
            self.vy = random.randint(0, 6) - 3


    def move(self):
        self.x += self.vx
        self.y += self.vy

        # If enemy ball move to outside the frame, multiply velocity to -1 to change direction
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1
        elif self.y - self.radius <= 0:
            self.y = self.radius
            self.vy *= -1
        elif self.x + self.radius >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vx *= -1
        elif self.y + self.radius >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.vy *= -1


def show_menu(screen):
    screen.fill((255, 181, 197))
    font = pygame.font.SysFont("monospace", 50, bold = True)
    title = font.render("Main Menu", 1, (0, 0, 0))
    screen.blit(title, (230, 20))

    font = pygame.font.SysFont("monospace", 30)
    play = font.render("P - Play", 1, (0, 0, 0))
    screen.blit(play, (240, 120))

    quit = font.render("Q - Quit", 1, (0, 0, 0))
    screen.blit(quit, (240, 220))

    save = font.render("S - Save Scores", 1, (0, 0, 0))
    screen.blit(save, (240, 320))

    view = font.render("V - View Scores", 1, (0, 0, 0))
    screen.blit(view, (240, 420))


    # Ideas:
    # 0: No choice
    # 1: Play
    # 2: Quit
    # 3: Save high scores
    # 4: View high scores

    res = 0

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_p]:
        res = 1
    elif pressed[pygame.K_q]:
        res = 2
    elif pressed[pygame.K_s]:
        res = 3
    elif pressed[pygame.K_v]:
        res = 4

    pygame.display.flip()
    clock.tick(60)
    return res


# Create a function to save high score to a file
def save_score(high_scores):
    f = open("score.txt", "w")
    for score in high_scores:
        f.write(score[0] + " " + str(score[1]))
    f.close()


# Create a function to update scores in rank
def update_scores(high_scores, score):
    for rank in range(len(high_scores)):
        if score[1] > high_scores[rank][1]:
            high_scores = high_scores[0: rank] + [score] + high_scores[rank: -1]
            break
    return high_scores


def read_scores():
    if os.path.isfile("score.txt"):
        f = open("score.txt", "r")
        high_scores = []
        for line in f:
            score = line.split()
            high_scores.append[score[0], int(score[1])]
        f.close()
        return high_scores
    else:
        return [("Player", 0), ("Player", 0), ("Player", 0)]

def score_saved_screen(won):
    screen.fill((250,128,114))
    text = "    Score Saved"
    text2 = ""
    if not won:
        text = "You must have won"
        text2 = "to save scores"

    font = pygame.font.SysFont("monospace", 30)
    displayed_text = font.render(text, 1, (0, 0, 0))
    screen.blit(displayed_text, (200, 200))

    displayed_text = font.render(text2, 1, (0, 0, 0))
    screen.blit(displayed_text, (200, 300))

    pygame.display.flip()
    pygame.time.delay(2000)


def view_high_scores(screen):
    screen.fill((135,206,255))

    high_score = read_scores()
    # View top 3 highest scores in rank
    s1 = high_score[0][0] + ": " + str(high_score[0][1])
    s2 = high_score[1][0] + ": " + str(high_score[1][1])
    s3 = high_score[2][0] + ": " + str(high_score[2][1])

    font = pygame.font.SysFont("monospace", 50)
    title = font.render("-- HIGHEST SCORES --", 1, (0, 0, 0))
    screen.blit(title, (300, 50))

    font = pygame.font.SysFont("monospace", 30)
    view_s1 = font.render(s1, 1, (0, 0, 0))
    screen.blit(view_s1, (300, 150))

    view_s2 = font.render(s2, 1, (0, 0, 0))
    screen.blit(view_s2, (300, 200))

    view_s3 = font.render(s3, 1, (0, 0, 0))
    screen.blit(view_s3, (300, 250))

    pygame.display.flip()
    pygame.time.delay(2000)


sys.stdout.write("Please enter your name: ")
name = input()


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(0)

score = 0
clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace", 20)

done = False

player_ball = PlayerBall(200, 100, 25, (0, 0, 255), screen)
health_ball = HealthBall(650, 300, 10, (100, 200, 0), screen)
enemy_ball = EnemyBall(350, 450, 60, (255, 0, 100), screen)

menu_choice = 0

# Time related variables (in milliseconds)
end_time = 20    # Limit time in 20 seconds
start_time = pygame.time.get_ticks()


high_scores = read_scores()

won = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # Show menu layer
    if menu_choice != 1:
        menu_choice = show_menu(screen)
        if menu_choice == 1:
            score = 0
            won = False
            start_time = pygame.time.get_ticks()

        elif menu_choice == 2:
            done = True
        elif menu_choice == 3:
            if won:
                save_score(high_scores)
            score_saved_screen(won)
        elif menu_choice == 4:
            view_high_scores(screen)
        continue
    
    # Condition about score and time to determine winners
    if -100 < score < 200 and pygame.time.get_ticks() < start_time + end_time * 1000:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            player_ball.move("UP")
        elif pressed[pygame.K_DOWN]:
            player_ball.move("DOWN")
        elif pressed[pygame.K_LEFT]:
            player_ball.move("LEFT")
        elif pressed[pygame.K_RIGHT]:
            player_ball.move("RIGHT")

        myfont = pygame.font.SysFont("monospace", 20)
        score_show = myfont.render("SCORE = " + str(score), 1, (0, 0, 0))
        screen.blit(score_show, (550, 460))

        passed_time = pygame.time.get_ticks() - start_time # calculate passed time
        time_left = passed_time / 1000    # convert miliseconds into seconds
        time_left = int(end_time - time_left)   # true time left
        time_show = myfont.render("Time: " + str((time_left + 1)), 1, (0, 0, 0))
        screen.blit(time_show, (10, 20))

        # Call move function of enemy and health to update position
        enemy_ball.move()
        health_ball.move()

        # Update score
        score += player_ball.collision_check(health_ball, enemy_ball)

        # Draw all figures
        player_ball.draw()
        health_ball.draw()
        enemy_ball.draw()

        # Update the cooldowns for touching health and enemy ball
        if player_ball.health_cooldown > 0:
            player_ball.health_cooldown -= 1
        if player_ball.enemy_cooldown > 0:
            player_ball.enemy_cooldown -= 1


    else:
        myfont = pygame.font.SysFont("monospace", 70, bold = True)

        if score < 100:
            text = myfont.render("YOU LOSE!", 1, (255, 0, 0))
            screen.blit(text, (180, 220))

        else:
            text = myfont.render("YOU WIN!!!", 1, (238, 118, 0))
            won = True
            # Call update_scores function to update new high score if player wins
            high_scores = update_scores(high_scores, (name, score))
            screen.blit(text, (180, 220))
        
        menu_choice = 0
        pygame.display.flip()
        clock.tick(70)
        pygame.time.delay(3000)
        continue

    pygame.display.flip()
    clock.tick(70)
