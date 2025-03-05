import pygame
import sys
import subprocess

pygame.init()

# this is the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Selection")

# boundaries colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

global image

# these are the 4 characters that are loaded
character_images = [
    pygame.image.load('1.png'),
    pygame.image.load('2.png'),
    pygame.image.load('3.png'),
    pygame.image.load('4.png')
]

# this is resizing the characters so they can all fit
character_images = [pygame.transform.scale(img, (100, 100)) for img in character_images]

# this is where the characters are on the display
image_positions = [(100, 200), (300, 200), (500, 200), (700, 200)]

# this makes it say choose your character at the top 
font = pygame.font.Font(None, 36)  
text = font.render("Choose your Character", True, WHITE) 

def game_loop():
    selected_character = None  # Variable to store selected character index
    running = True

    while running:
        screen.fill(BLACK)  # This makes the screen bloack

        # This is the positioning of the text
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))  

        # This opens the characters image files
        for i, (img, pos) in enumerate(zip(character_images, image_positions)):
            screen.blit(img, pos)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if mouse click is within one of the character image rectangles
                for i, pos in enumerate(image_positions):
                    rect = pygame.Rect(pos[0], pos[1], 100, 100) 
                    if rect.collidepoint(mouse_pos):
                        selected_character = i  # Store the selected character index
                        if (selected_character == 0):
                            f = open("character.txt", "w")
                            f.write("1.png")
                            f.close()
                            subprocess.Popen([sys.executable, './maze.py', '--username', 'root'])
                        elif (selected_character == 1):
                            f = open("character.txt", "w")
                            f.write("2.png")
                            f.close()
                            subprocess.Popen([sys.executable, './maze.py', '--username', 'root'])
                        elif (selected_character == 2):
                            f = open("character.txt", "w")
                            f.write("3.png")
                            f.close()
                            subprocess.Popen([sys.executable, './maze.py', '--username', 'root'])
                        elif (selected_character == 3):
                            f = open("character.txt", "w")
                            f.write("4.png")
                            f.close()
                            subprocess.Popen([sys.executable, './maze.py', '--username', 'root'])

        pygame.display.flip() 

    return selected_character


selected = game_loop()

pygame.quit()
sys.exit()