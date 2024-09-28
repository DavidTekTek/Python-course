import pygame
import sys

# Initialize Pygame
pygame.init()

# Window parameters
window_size = (500, 500)
caption = "My First Game Screen"
background_color = (58, 58, 58)

# Create the game window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(caption)

# Load and resize the image
image = pygame.image.load("3gq9yesj.png")  # Replace with your image file path
image = pygame.transform.scale(image, (300, 300))

# Calculate image position to center it
image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Blit the image to the screen (draw it)
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()