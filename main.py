import pygame
import sys

from colors import Colors
from game import Game

GAME_UPDATE = pygame.USEREVENT + 1

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.WHITE.value)
score_rect = pygame.Rect(320, 55, 170, 60)
next_block_surface = title_font.render("Next", True, Colors.WHITE.value)
next_block_rect = pygame.Rect(320, 215, 170, 180)
game_over_surface = title_font.render("GAME OVER", True, Colors.WHITE.value)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Pytetris")
clock = pygame.time.Clock()
pygame.time.set_timer(GAME_UPDATE, 600)

game = Game()

events_to_listen = [pygame.QUIT, pygame.KEYDOWN, GAME_UPDATE]

pygame.event.clear()
while True:
    for event in pygame.event.get(eventtype=events_to_listen):
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()
            case pygame.KEYDOWN if not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)  # Points for moving down
                if event.key == pygame.K_UP:
                    game.rotate()
            case pygame.KEYDOWN if game.game_over and event.key == pygame.K_RETURN:
                game.reset()
            case GAME_UPDATE if not game.game_over:
                game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Colors.WHITE.value)

    screen.fill(Colors.DARK_BLUE.value)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_block_surface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.LIGHT_BLUE.value, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.LIGHT_BLUE.value, next_block_rect, 0, 10)

    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx,
            centery=score_rect.centery,
        ),
    )

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
