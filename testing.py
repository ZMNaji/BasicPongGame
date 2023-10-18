import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)

# Paddle properties
paddle_width = 10
paddle_height = 100
paddle_speed = 5

# Ball properties
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_velocity_x = 5
ball_velocity_y = 5

# Paddle positions
left_paddle_x = 20
left_paddle_y = (screen_height - paddle_height) // 2

right_paddle_x = screen_width - 20 - paddle_width
right_paddle_y = (screen_height - paddle_height) // 2

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed

    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check for collisions with the paddles
    left_paddle_rect = pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    right_paddle_rect = pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height)

    if left_paddle_rect.colliderect(
        ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius
    ) or right_paddle_rect.colliderect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius):
        ball_velocity_x *= -1  # Reverse the horizontal velocity on paddle collision

    # Check for collisions with the top and bottom walls
    if ball_y + ball_radius >= screen_height or ball_y - ball_radius <= 0:
        ball_velocity_y *= -1  # Reverse the vertical velocity on wall collision

    # Fill the screen with white
    screen.fill("black")

    # Draw paddles
    pygame.draw.rect(screen, (0, 0, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 0, 0), (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, (0, 255, 0), (ball_x, ball_y), ball_radius)
    clock.tick(40)
    # Update the display
    pygame.display.update()
