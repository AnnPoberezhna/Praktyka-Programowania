import pygame
import numpy as np
import time

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE

# COLORS
BLACK = (0, 0, 0) #grid
GRAY = (128, 128, 128) #background
GREEN = (0, 128, 0) #alive cells

def update(screen, cells, size):
    next_cells = np.zeros((cells.shape[0], cells.shape[1]))

    screen.fill(GRAY)

    for row, col in np.ndindex(cells.shape):
        num_alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        if cells[row, col] == 1:
            if num_alive < 2 or num_alive > 3:
                next_cells[row, col] = 0
            else:
                next_cells[row, col] = 1
        else:
            if num_alive == 3:
                next_cells[row, col] = 1
        
        if cells[row, col] == 1:
            pygame.draw.rect(screen, GREEN, (col*size, row*size, size - 1, size - 1))
    
    for x in range(0, WIDTH, size):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, size):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

    return next_cells

def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Grid initialization
    cells = np.random.choice([0, 1], size=(GRID_HEIGHT, GRID_WIDTH), p=[0.8, 0.2]) # 20% being alive

    running = True
    playing=True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

        if playing:
            cells = update(screen, cells, TILE_SIZE)
            pygame.display.flip()
            time.sleep(1)
        else:
            update(screen, cells, TILE_SIZE)
            pygame.display.flip()

if __name__ == "__main__":
    main()
    