import pygame
import random
import math


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


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

score = 0
clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace", 20)

done = False

player_ball = PlayerBall(200, 100, 25, (0, 0, 255), screen)
health_ball = HealthBall(650, 300, 10, (100, 200, 0), screen)
enemy_ball = EnemyBall(350, 450, 40, (255, 0, 100), screen)

menu_choice = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # Show menu layer
    if menu_choice != 1:
        menu_choice = show_menu(screen)
        if menu_choice == 2:
            done = True
        continue

    if score > -100 and score < 100:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            player_ball.move("UP")
        elif pressed[pygame.K_DOWN]:
            player_ball.move("DOWN")
        elif pressed[pygame.K_LEFT]:
            player_ball.move("LEFT")
        elif pressed[pygame.K_RIGHT]:
            player_ball.move("RIGHT")


        score_show = myfont.render("SCORE = " + str(score), 1, (0, 0, 0))
        screen.blit(score_show, (550, 460))

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

        if score == -100:
            text = myfont.render("YOU LOSE!", 1, (255, 0, 0))
            screen.blit(text, (180, 220))

        if score == 100:
            text = myfont.render("YOU WIN!!!", 1, (238, 118, 0))
            screen.blit(text, (180, 220))

    pygame.display.flip()
    clock.tick(60)
