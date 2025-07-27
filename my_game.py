import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 750
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Honor Score")
pygame.display.set_caption("Catch the Falling ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_width = 80
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 8

# Falling ball
ball_width = 30
ball_height = 30
ball_x = random.randint(0, WIDTH - ball_width)
ball_y = 0
ball_speed = 6

# Score
score = 0
win_score = 500
lives = 3 #player starts with 3 lives
font = pygame.font.SysFont(None, 36)
honor_score = 0

# Game loop
running = True
while running:
    screen.fill(WHITE) 

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move ball
    ball_y += ball_speed

    # Check catch
    if (player_y < ball_y + ball_height and
        player_y + player_height > ball_y and
        player_x < ball_x + ball_width and
        player_x + player_width > ball_x):
        score += 1
        ball_x = random.randint(0, WIDTH - ball_width)
        ball_y = 0

    # Missed catch
    if ball_y > HEIGHT:
        lives -= 1 #lose one life
        if lives <= 0:
            # show "You Lose!" message
            screen.fill(WHITE)
            lose_text = font.render("You Lose!",True, (255,0,0))
            honor_text = font.render(f"Honor Score:{score}", True,(0,0,0))
            screen.blit(lose_text, (WIDTH //2 - 80, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(3000) # wait 3 seconds
            running = False # Exit game
        else:
            # Reset ball position
            ball_x = random.randint(0, WIDTH - ball_width)
            ball_y = 0

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw  ball
    pygame.draw.rect(screen, RED, (ball_x, ball_y, ball_width, ball_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    def show_honor_score(score):
        score_text = font.render(f"Honor Score:{score}",True, (255,255,255)) # White text
    screen.blit(score_text, (10, 10))
    if score >= win_score:
        screen.fill(WHITE)
        win_text = font.render("you Win!",True,(0,255,0))
        honor_text = font.render(f"Honor Score:{score}",True,(0,0,0))
        screen.blit(win_text,(WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(3000) # wait 3 seconds
        running = False # Exit game

    # Update screen
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
