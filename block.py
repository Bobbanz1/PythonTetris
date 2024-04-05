from colors import Colors
import pygame
from position import Position


class Block:
    def __init__(self, id):
        # Used to distinguish between different blocks
        self.id = id
        # Used to store the occupied cells in the bounding grid for each rotation state of the block
        self.cells = {}
        # Width and Height of each block
        self.cell_size = 30
        # Rotation state of the block
        self.rotation_state = 0
        # All the colors the block can have
        self.colors = Colors.get_cell_colors()

        # Used to move the block around
        self.row_offset = 0
        self.column_offset = 0

    # Move the block around
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # Get the cell positions
    def get_cell_positions(self):
        # List of positions for this rotation state
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            # New position
            position = Position(
                position.row + self.row_offset, position.column + self.column_offset
            )
            # Append it to the moved tiles
            moved_tiles.append(position)
        return moved_tiles

    # Rotate the block
    def rotate(self):
        self.rotation_state += 1
        # If we're outside the amount of rotations we can handle then reset it to zero
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Undo the rotation
    def undo_rotation(self):
        self.rotation_state -= 1
        # If we're outside the amount of rotations we can handle then reset it to zero
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Draw the block
    def draw(self, screen, offset_x, offset_y):
        # Gets the list of positions for this rotation state
        tiles = self.get_cell_positions()
        # Draw the rectangles for each tile
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
