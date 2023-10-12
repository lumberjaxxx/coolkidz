import pygame
import random

class BouncingBall:

    def __init__(self, screen, color, size, x, y):
        self.screen = screen
        self.color = color
        self.size = size
        self.position = pygame.Vector2(x, y)
        self._speedx = random.randint(1, 101)
        self._speedy = random.randint(1, 101)
        self.active = True
        self.dt= 0

    def move(self,dt):
        if not self.active:
            return
        # y = 10
        # x = 10
        self.position.y += self._speedy 
        self.position.x += self._speedx 
        if self.position.y >= 720:
            self._speedy = -self._speedy
        if self.position.y <= 0:
            self._speedy = -self._speedy
        if self.position.x >= 1280:
            self._speedx = -self._speedx
        if self.position.x <= 0:
            self._speedx = -self._speedx


    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)
    
    def fps(self):
        pygame.time.delay(random.randint(-10,1))


pygame.init()
screen = pygame.display.set_mode((1280, 720))
# speed = 300
# x = random.randint(1,11)
# y = random.randint(1,721)
clock = pygame.time.Clock()
running = True


b1 = BouncingBall(screen, "red", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b2 = BouncingBall(screen, "green", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b3 = BouncingBall(screen, "sky blue", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b4 = BouncingBall(screen, "pink", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b5 = BouncingBall(screen, "yellow", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b6 = BouncingBall(screen, "black", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b7 = BouncingBall(screen, "cyan", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b8 = BouncingBall(screen, "brown", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b9 = BouncingBall(screen, "magenta", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b10 = BouncingBall(screen, "white", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b11 = BouncingBall(screen, "yellow", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b12 = BouncingBall(screen, "black", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b13 = BouncingBall(screen, "cyan", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b14 = BouncingBall(screen, "brown", random.randint(30,151), random.randint(1,1281), random.randint(1,721))
b15 = BouncingBall(screen, "magenta", random.randint(30,151), random.randint(1,1281), random.randint(1,721))


balls = [b1, b2, b3, b4,b5,b6,b7,b8,b9,b10, b11,b12,b13,b14,b15]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    for ball in balls:
        ball.move(ball.dt)
        ball.draw()
        ball.fps()

    pygame.display.flip()

    for player in balls:
        player.dt = clock.tick(150) / 1000

pygame.quit()