import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (50, 150, 200)
OBJECT_COLOR = (255, 255, 255)  # White objects
BASKET_COLOR = (255, 200, 0)  # Yellow basket
FPS = 60

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch the Falling Objects')

# Basket settings
basket_width, basket_height = 100, 20
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 7

# Object settings
object_width, object_height = 20, 20
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = 0
object_speed = 5

# Font setup for feedback messages
pygame.font.init()  # Initialize the font module
font = pygame.font.Font(None, 36)  # Create a font object from the default font

# Message display settings
message_display_time = 90
current_message_time = 0
message = None

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
        basket_x += basket_speed

    # Object movement
    object_y += object_speed
    if object_y + object_height > SCREEN_HEIGHT:  # Miss condition
        if not message:  # Update message if there isn't one being displayed
            message = font.render('Missed!', True, (255, 0, 0))
        current_message_time = message_display_time  # Reset the message timer
        object_y = 0
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
    elif basket_y < object_y + object_height and basket_x < object_x + object_width and basket_x + basket_width > object_x:
        if not message:
            message = font.render('Caught!', True, (0, 255, 0))
        current_message_time = message_display_time
        object_y = 0
        object_x = random.randint(0, SCREEN_WIDTH - object_width)

    # Fill the background
    screen.fill(BG_COLOR)

    # Draw the basket
    pygame.draw.rect(screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.rect(screen, OBJECT_COLOR, (object_x, object_y, object_width, object_height))

    # Display the message if there is one
    if message and current_message_time > 0:
        screen.blit(message, (10, 50))
        current_message_time -= 1
    elif current_message_time <= 0:
        message = None  # Clear the message when the time expires

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
