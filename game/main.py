import pygame
from random import randrange


WIDTH = 1200
HEIGHT = 800
FPS = 60

paddle_w = 330
paddle_h = 35
paddle_speed = 35
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h )

ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(randrange(30, 256), randrange(30, 256), randrange(30, 256)) for i in range(10) for j in range(4)]

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg_img = pygame.image.load("assets/bg.png").convert()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(bg_img, (0, 0))

    [pygame.draw.rect(window, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(window, pygame.Color(236, 240, 36), paddle)
    pygame.draw.circle(window, pygame.Color(209, 25, 25), ball.center, ball_radius)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius:
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dy = -dy

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
