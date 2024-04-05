# Grid where the tetris blocks are going to fall down on.
import pygame
from colors import Colors


class Grid:
    def __init__(self):
        # Number of rows in the game
        self.num_rows = 20
        # How many columns in the game
        self.num_cols = 10
        # How big a cell is
        self.cell_size = 30
        # The grid itself
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # All the colors in the world, in the palm of my hand.
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Used to check if the section the block is trying to go is empty or not.
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # Used to check if the row is full
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # Used to clear the row if it is full
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # Move the uppoer row down if it is not full
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # Used to clear rows
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            # Check if this row is full, if it is then clear it
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # Reset the grid
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen, offset_x, offset_y):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    offset_x + column * self.cell_size,
                    offset_y + row * self.cell_size,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                # Draws the rectangle onto the screen, the color is based on the cell_value so if it's zero then it's gray and so forth
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
