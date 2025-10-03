import pygame, random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Paddle Class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.speed = 7

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.y > 0:
            self.y -= self.speed
        if keys[down_key] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self):
        self.radius = 10
        self.restart()

    def restart(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def move(self, paddle_1, paddle_2):
        self.x += self.speed_x
        self.y += self.speed_y

        # wall collision
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

        # paddle collision
        if self.speed_x < 0 and paddle_1.y <= self.y <= paddle_1.y + paddle_1.height and self.x - self.radius <= paddle_1.x + paddle_1.width:
            self.speed_x = -self.speed_x
        if self.speed_x > 0 and paddle_2.y <= self.y <= paddle_2.y + paddle_2.height and self.x + self.radius >= paddle_2.x:
            self.speed_x = -self.speed_x

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)


player_1 = Paddle(0, SCREEN_HEIGHT // 2 - 50)
player_2 = Paddle(SCREEN_WIDTH - 10, SCREEN_HEIGHT // 2 - 50)
ball = Ball()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player moves
    player_2.move(pygame.K_UP, pygame.K_DOWN)
    player_1.move(pygame.K_w, pygame.K_s)
    ball.move(player_1, player_2)

    # check for point
    if ball.x < 0:
        ball.restart()
    elif ball.x > SCREEN_WIDTH:
        ball.restart()

    screen.fill((0,0,0))

    # Player draw
    player_1.draw()
    player_2.draw()
    ball.draw()

    pygame.display.flip()
pygame.quit()