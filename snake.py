import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Initialize the mixer module for playing background music
pygame.mixer.init()

# Load and play background music in a loop
pygame.mixer.music.load('snakebm.mp3')  
pygame.mixer.music.play(-1) 

# Set the speed of the snake
snake_speed = 15

# Set the dimensions of the game window
window_x = 600
window_y = 600

# Define color variables using RGB format
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the title of the game window
pygame.display.set_caption('GeeksforGeeks Snakes')

# Create the game window with the specified dimensions
game_window = pygame.display.set_mode((window_x, window_y))

# Load the background image
background_image = pygame.image.load('asd.jpg')  

# Create a clock object to control the game's frame rate
fps = pygame.time.Clock()

# Initial position of the snake's head
snake_position = [100, 50]

# Initial snake body, represented as a list of positions (x, y)
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# Position of the first fruit
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

# Boolean flag to determine if the fruit should spawn
fruit_spawn = True

# Initial direction of the snake's movement
direction = 'RIGHT'
change_to = direction

# Initialize the score
score = 0

# Function to display the score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)  # Set the font for the score
    score_surface = score_font.render('Score : ' + str(score), True, color)  # Create the score surface
    score_rect = score_surface.get_rect()  # Get the rectangle for positioning
    game_window.blit(score_surface, score_rect)  # Display the score on the game window

# Function to handle the game over scenario
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)  # Set the font for the game over message
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)  # Create the game over surface
    game_over_rect = game_over_surface.get_rect()  # Get the rectangle for positioning
    game_over_rect.midtop = (window_x/2, window_y/4)  # Position the message at the top center of the screen
    game_window.blit(game_over_surface, game_over_rect)  # Display the game over message
    pygame.display.flip()  # Update the display
    time.sleep(2)  # Wait for 2 seconds
    pygame.quit()  # Quit the game
    quit()  # Exit the program

# Main game loop
while True:
    # Event handling to check for user input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update the direction based on user input, preventing reverse direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake's position based on the direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Update the snake's body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10  # Increase the score when the snake eats the fruit
        fruit_spawn = False  # Set fruit spawn to False to create a new fruit
        snake_speed += 2  # Increase the snake's speed
    else:
        snake_body.pop()  # Remove the last part of the snake's body to keep the length consistent

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]  # Generate new fruit position
    fruit_spawn = True

    # Display the background image
    game_window.blit(background_image, (0, 0))
    
    # Draw the snake and fruit on the game window
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for collision with the boundaries of the game window
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Check for collision with the snake's body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display the current score
    show_score(1, white, 'times new roman', 20)

    # Update the display and set the frame rate
    pygame.display.update()
    fps.tick(snake_speed)
