import pygame

# Initialize Pygame
pygame.init()

# Set up window dimensions
window_width = 600
window_height = 400

# Create a window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Text Display")

# Set background color (white)
white = (255, 255, 255)
screen.fill(white)

# Define text and font
font = pygame.font.SysFont('Arial', 50)  # You can try different fonts
text = "Hello, Pygame!"
text_color = (0, 0, 0)  # Black text color

# Render the text
text_surface = font.render(text, True, text_color)

# Get the text rectangle (for positioning)
text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))

# Main loop to display the text on the window
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the window is closed
            running = False

    # Fill the background with white
    screen.fill(white)
    
    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
