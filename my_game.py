import pygame
import random

# Initialize Pygamebg
pygame.init()
catch_sound = pygame.mixer.Sound(r"C:/Users/ADMIN/Music/WhatsApp Audio 2025-09-21 at 09.19.53_35294b28.mp3")
drop_sound = pygame.mixer.Sound(r"C:/Users/ADMIN/Music/WhatsApp Audio 2025-09-21 at 09.19.58_dafccb4f.mp3")
bg = pygame.image.load(r"C:/Users/ADMIN/Music/WhatsApp Image 2025-12-07 at 16.00.52_7a4da6c8.jpg")
# Screen dimensions
WIDTH = 700
HEIGHT = 650
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
player_speed = 9

# Falling ball
ball_width = 30
ball_height = 30
ball_x = random.randint(0, WIDTH - ball_width)
ball_y = 0
ball_speed = 9

# Score
score = 0
win_score = 50
lives = 3 #player starts with 3 lives
font = pygame.font.SysFont(None, 36)
honor_score = 0

# Game loop
running = True
game_over = False
while running:
    screen.blit(bg, (0, 0))  # load image

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
        catch_sound.play() # play catch sound
        ball_x = random.randint(0, WIDTH - ball_width)
        ball_y = 0

    # Missed catch
    if ball_y > HEIGHT:
        drop_sound.play() # play drop sound
        game_over = True
        lives -= 1 #lose one life
        if lives <= 0:
            # show "You Lose!" message
            screen.blit(bg, (0, 0)) # load image
            lose_text = font.render("You Lose!",True, (255,0,0))
            honor_text = font.render(f"Honor Score:{score}", True,(255,255,255))
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
        screen.blit(bg, (0, 0)) #load image
        win_text = font.render("you Win!",True,(0,255,0))
        honor_text = font.render(f"Honor Score:{score}",True,(255,255,255))
        screen.blit(win_text,(WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(3000) # wait 3 seconds
        running = False # Exit game

    # Update screen
    pygame.display.flip()
    clock.tick(FPS)

    

if game_over:
    # Show lose message
    lose_text = font.render("YOU LOSE - Press R to Restart", True, (255,0,0))
    screen.blit(lose_text, (WIDTH // 2 - 250, HEIGHT // 2))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        # Reset game variables
        score = 0
        ball_x = random.randint(0, WIDTH - ball_width)
        ball_y = 0
        player_x = WIDTH // 2 - player_width // 2
        game_over = False
    
pygame.quit()



