import pygame

# Create a class called Ball to set up for player's ball as well as target ball
class Ball:
	def __init__(self, x, y, radius, screen):
		self.x = x      # x, y are coordinates of ball center
		self.y = y
		self.radius = radius
		self.screen = screen

	def draw(self):
        # Draw a blue circle
		pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.radius)

pygame.init()
# Set width and height of the screen
screen = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()     # Create a clock to keep track of time
ball1 = Ball(100, 100, 20, screen)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0, 0, 0))      # fill the screen with white color

    ball1.draw()

    pygame.display.flip()       # update the screen
    clock.tick(60)      # limit the numbers of frames that program runs are always under 60. It's used to update the clock
