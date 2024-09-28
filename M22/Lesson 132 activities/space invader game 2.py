import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Background color
background_color = (0, 0, 0)

# Background sound
mixer.music.load('background.wav')  # Add a background sound file if you have it
mixer.music.play(-1)  # Play in a loop

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')  # Add your icon file path
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player.png')  # Add your player image path
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))  # Add your enemy image path
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load('bullet.png')  # Add your bullet image path
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 0.8
bullet_state = "ready"  # "ready" means you can't see the bullet, "fire" means the bullet is currently moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Function to display the score
def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to display game over text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Function to draw the player
def player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw the enemy
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Function to fire the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Function to detect collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27

# Main Game Loop
running = True
while running:
    # Fill the screen with the background color
    screen.fill(background_color)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change

    # Boundary checking for player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i]

        # Collision detection
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Draw player
    player(player_x, player_y)

    # Show score
    show_score(text_x, text_y)

    # Update the screen
    pygame.display.update()

pygame.quit()
