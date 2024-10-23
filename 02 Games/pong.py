import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Ball variables
ball_x = width // 2
ball_y = height // 2
ball_dx = 10 * random.choice((1, -1))
ball_dy = 10 * random.choice((1, -1))
ball_radius = 10

# Paddle variables
paddle_width = 20
paddle_height = 100
player_x = 50
player_y = height // 2 - paddle_height // 2
opponent_x = width - 50 - paddle_width
opponent_y = height // 2 - paddle_height // 2
paddle_speed = 7

# Scoring
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

# Game loop
run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= paddle_speed
    if keys[pygame.K_s] and player_y < height - paddle_height:
        player_y += paddle_speed
    if opponent_y + paddle_height // 2 < ball_y:
        opponent_y += paddle_speed
    if opponent_y + paddle_height // 2 > ball_y:
        opponent_y -= paddle_speed

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top/bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_dy *= -1

    # Ball collision with paddles
    if (player_x < ball_x - ball_radius < player_x + paddle_width and
        player_y < ball_y < player_y + paddle_height):
        ball_dx *= -1

    if (opponent_x < ball_x + ball_radius < opponent_x + paddle_width and
        opponent_y < ball_y < opponent_y + paddle_height):
        ball_dx *= -1

    # Scoring
    if ball_x < 0:
        opponent_score += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dx *= random.choice((1, -1))
    if ball_x > width:
        player_score += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dx *= random.choice((1, -1))

    # Drawing everything
    win.fill(black)
    pygame.draw.rect(win, white, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(win, white, (opponent_x, opponent_y, paddle_width, paddle_height))
    pygame.draw.circle(win, white, (ball_x, ball_y), ball_radius)
    player_text = font.render(str(player_score), True, white)
    opponent_text = font.render(str(opponent_score), True, white)
    win.blit(player_text, (width // 4, 20))
    win.blit(opponent_text, (width * 3 // 4, 20))

    # Refresh the screen
    pygame.display.update()

# Quit the game
pygame.quit()
