import pygame, sys
from game import Game
from colors import Colors

# Definitions

pygame.init()

# Title font
title_font = pygame.font.Font(None, size=40)

# Score here
score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(11, 55, 170, 60)

# Next block here
next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(11, 215, 170, 180)

# Game over here
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# The window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

# The game class here is used to make the code more readable
game = Game()

# Custom event
GAME_UPDATE = pygame.USEREVENT

# Update the GAME_UPDATE every 200 miliseconds
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop here
while True:
    for event in pygame.event.get():
        # Used to make the game stay open until the player closes it manually
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move the block around using arrow keys
        if event.type == pygame.KEYDOWN:
            # If the game is over then reset it
            if game.game_over == True:
                game.game_over = False
                game.reset()
            # Better than a bunch of conditionals
            match event.key:
                case pygame.K_LEFT:
                    if game.game_over == False:
                        game.move_left()
                case pygame.K_RIGHT:
                    if game.game_over == False:
                        game.move_right()
                case pygame.K_DOWN:
                    if game.game_over == False:
                        game.move_down()
                        game.update_score(0, 1)
                case pygame.K_UP:
                    if game.game_over == False:
                        game.rotate()

        # Used to ensure the thing actually moves downwards, executes ONCE every 200 miliseconds
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Draw here
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (65, 20, 50, 50))
    screen.blit(next_surface, (75, 180, 50, 50))

    # Game over is hidden until needed
    if game.game_over == True:
        screen.blit(game_over_surface, (11, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    # Make the game update so stuff actually happens.
    pygame.display.update()

    # Framerate here
    # Runs 60 times per second.
    clock.tick(60)
