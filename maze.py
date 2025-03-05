import pygame
import random
import sys
import pickle
import os

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
CELL_SIZE = WIDTH // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

f = open("character.txt", "r")
player_image = pygame.image.load(f.read())
scale_factor = 1.5  
player_image = pygame.transform.scale(player_image, (CELL_SIZE * scale_factor, CELL_SIZE * scale_factor))

MAZE_FILE = "saved_maze.pkl"

def generate_maze():
    maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def carve(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                maze[x + dx][y + dy] = 0
                carve(nx, ny)

    start_x, start_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    maze[start_x][start_y] = 0
    carve(start_x, start_y)
    return maze

def save_maze(maze):
    with open(MAZE_FILE, 'wb') as f:
        pickle.dump(maze, f)

def load_maze():
    if os.path.exists(MAZE_FILE):
        with open(MAZE_FILE, 'rb') as f:
            return pickle.load(f)
    return None

def draw_maze(maze, exit_position):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    exit_x, exit_y = exit_position
    pygame.draw.rect(screen, BLUE, (exit_x * CELL_SIZE, exit_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def extra_life_screen():
    font = pygame.font.Font(None, 74)
    message = font.render("Extra Life!", True, YELLOW)
    return message

def main():
    maze = load_maze()
    if maze is None:
        maze = generate_maze()
        save_maze(maze)

    player_x, player_y = 1, 1

    exit_x, exit_y = GRID_SIZE - 2, GRID_SIZE - 2

    while maze[exit_y][exit_x] == 1:
        exit_x, exit_y = GRID_SIZE - 2, GRID_SIZE - 2

    clock = pygame.time.Clock()
    running = True
    won = False
    in_extra_life_screen = False
    prev_x, prev_y = player_x, player_y

    while running:
        screen.fill(WHITE)

        if in_extra_life_screen:
            message = extra_life_screen()
            screen.blit(message, (WIDTH // 4, HEIGHT // 2))
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                in_extra_life_screen = False
                player_x, player_y = prev_x, prev_y
                continue

        else:
            draw_maze(maze, (exit_x, exit_y))
            screen.blit(player_image, (player_x * CELL_SIZE, player_y * CELL_SIZE))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            move_speed = 1

            if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y][player_x - move_speed] == 0:
                player_x -= move_speed
            if keys[pygame.K_RIGHT] and player_x < GRID_SIZE - 1 and maze[player_y][player_x + move_speed] == 0:
                player_x += move_speed
            if keys[pygame.K_UP] and player_y > 0 and maze[player_y - move_speed][player_x] == 0:
                player_y -= move_speed
            if keys[pygame.K_DOWN] and player_y < GRID_SIZE - 1 and maze[player_y + move_speed][player_x] == 0:
                    player_y += move_speed

            if (player_x, player_y) != (prev_x, prev_y):
                if player_x < prev_x or player_y < prev_y:
                    in_extra_life_screen = True

            prev_x, prev_y = player_x, player_y

            if player_x == exit_x and player_y == exit_y:
                won = True
                font = pygame.font.Font(None, 74)
                win_text = font.render("You Win!", True, BLUE)
                screen.blit(win_text, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
