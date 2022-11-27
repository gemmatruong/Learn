import pygame
import random
import math


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    def __init__(self, x, y, screen, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)

class PlayerBall(Ball):
    def __init__(self, x, y, screen, radius, color):
        super().__init__(x, y, screen, radius, color)
        self.cooldown1 = 0     # Add cooldown variable after touching health ball
        self.cooldown2 = 0     # Add cooldown variable after touching enemy ball


    def move(self, mv_type):
        if mv_type == "UP":
            self.y -= 4
        elif mv_type == "DOWN":
            self.y += 4
        elif mv_type == "LEFT":
            self.x -= 4
        elif mv_type == "RIGHT":
            self.x += 4

        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
        elif self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius

    def check_attack(self, health_ball, enemy_ball):
        # Use Euclidean distance to check if distance between two centers are less than sum of radius of two balls
        to_return = 0
        if math.sqrt((self.x - health_ball.x)**2 + (self.y - health_ball.y)**2) < self.radius + health_ball.radius:
            if self.cooldown1 == 0:
                self.cooldown1 = 10
                to_return += 10

        if math.sqrt((self.x - enemy_ball.x)**2 + (self.y - enemy_ball.y)**2) < self.radius + enemy_ball.radius:
            if self.cooldown2 == 0:
                self.cooldown2 = 10
                to_return -= 10

        return to_return


class HealthBall(Ball):
    def __init__(self, x, y, screen, radius, color):
        super().__init__(x, y, screen, radius, color)
        # Create vx and vy which are the velocity values of health ball. They are randomly chosen from [0, 4]
        self.vx = random.randint(0, 4)
        self.vy = random.randint(0, 4)

        while self.vx == 0 or self.vy == 0:
            self.vx = random.randint(0, 4) - 2
            self.vy = random.randint(0, 4) - 2
        
    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -1
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vx *= -1
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -1
        elif self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.vy *= -1

class EnemyBall(Ball):
    def __init__(self, x, y, screen, radius, color):
        super().__init__(x, y, screen, radius, color)
        self.vx = random.randint(0, 6)
        self.vy = random.randint(0, 6)

        while self.vx == 0 or self.vy == 0:
            self.vx = random.randint(0, 6) - 3
            self.vy = random.randint(0, 6) - 3

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -1
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vx *= -1
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -1
        elif self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.vy *= -1


def draw_gameover(screen, message):
    pygame.draw.rect(screen, (0, 0, 0), (140, 130, 440, 250), 0)

    font = pygame.font.SysFont("monospace", 60, bold = True)
    text = font.render("GAME OVER!", 1, (255, 0, 0))
    screen.blit(text, (180, 170))

    font = pygame.font.SysFont("monospace", 70, bold = True)
    text = font.render(message, 1, (20, 255, 100))
    screen.blit(text, (200, 280))



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

player_ball = PlayerBall(100, 100, screen, 20, (0, 0, 255))
health_ball = HealthBall(400, 400, screen, 10, (0, 255, 0))
enemy_ball = EnemyBall(400, 100, screen, 20, (255, 0, 0))


myfont = pygame.font.SysFont("monospace", 20)
score = 0
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        player_ball.move("UP")
    elif pressed[pygame.K_DOWN]:
        player_ball.move("DOWN")
    elif pressed[pygame.K_LEFT]:
        player_ball.move("LEFT")
    elif pressed[pygame.K_RIGHT]:
        player_ball.move("RIGHT")


    if -100 < score < 100:
        screen.fill((255, 255, 255))

        # Display the score on screen
        score_display = myfont.render("SCORE: " + str(score), 1, (0, 0, 0))
        screen.blit(score_display, (580, 480))

        health_ball.draw()
        player_ball.draw()
        enemy_ball.draw()

        health_ball.move()
        enemy_ball.move()

        score += player_ball.check_attack(health_ball, enemy_ball)

        if player_ball.cooldown1 > 0:
            player_ball.cooldown1 -= 1
        if player_ball.cooldown2 > 0:
            player_ball.cooldown2 -= 1

    else:
        screen.fill((255, 255, 255))
        if score == -100:
            message = "You Lose"
        elif score == 100:
            message = "You Win"
        draw_gameover(screen, message)


    pygame.display.flip()

    clock.tick(60)
