from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        # The grid of the game itself
        self.grid = Grid()
        # All the blocks in the world!
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        # Current block we have.
        self.current_block = self.get_random_block()
        # Upcoming block
        self.next_block = self.get_random_block()
        # The game over thingy
        self.game_over = False
        # Scoring
        self.score = 0

    # Score updater
    def update_score(self, lines_cleared, move_down_points):
        # Allows to add more score givers here, like 4 lines cleared, etc
        match lines_cleared:
            case 1:
                self.score += 100
            case 2:
                self.score += 300
            case 3:
                self.score += 500
        self.score += move_down_points

    # Randomizer
    def get_random_block(self):
        # If we ain't got blocks in the list anymore then recreate it
        if len(self.blocks) == 0:
            self.blocks = [
                IBlock(),
                JBlock(),
                LBlock(),
                OBlock(),
                SBlock(),
                TBlock(),
                ZBlock(),
            ]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Movement section

    # Move left
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    # Move right
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    # Move downwards
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # Rotate
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    # Lock the block into place once it reaches the bottom
    def lock_block(self):
        # Get the current position of the block
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # Produce the next block
        self.current_block = self.next_block
        # Randomize the next block so we will always have a randomized block
        self.next_block = self.get_random_block()
        # Check if we need to clear the row because it is full
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        # If we can't fit the block then game over.
        if self.block_fits() == False:
            self.game_over = True

    # Checks to see if the block fits or not
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    # Is the block inside the game window
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # Reset the game
    def reset(self):
        self.grid.reset()
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        # Reset score to 0
        self.score = 0

    # Draw this stuff
    def draw(self, screen):
        self.grid.draw(screen, 190, 11)
        self.current_block.draw(screen, 190, 11)
        self.next_block.draw(screen, -45, 270)
