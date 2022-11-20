import pygame

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

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

player_ball = PlayerBall(100, 100, screen, 20, (0, 0, 255))

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
    
    screen.fill((255, 255, 255))

    player_ball.draw()

    pygame.display.flip()

    clock.tick(60)
