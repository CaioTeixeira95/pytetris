from random import choice

import pygame

from blocks import Block, LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock
from grid import Grid


class Game:
    grid: Grid
    blocks: list[Block]
    current_block: Block
    next_block: Block
    game_over: bool
    score: int
    rotate_sound: pygame.mixer.Sound
    clear_sound: pygame.mixer.Sound

    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            LBlock(),
            JBlock(),
            IBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
        pygame.mixer_music.load("sounds/music.ogg")
        pygame.mixer_music.play(-1)

    def update_score(self, lines_cleared: int, move_down_points: int):
        match lines_cleared:
            case 1:
                self.score += 100
            case 2:
                self.score += 300
            case _ if lines_cleared > 3:
                self.score += 500
        self.score += move_down_points

    def get_random_block(self) -> Block:
        if not self.blocks:
            self.blocks = [
                LBlock(),
                JBlock(),
                IBlock(),
                OBlock(),
                SBlock(),
                TBlock(),
                ZBlock(),
            ]

        block = choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside_boundary() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside_boundary() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside_boundary() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)

        if not self.block_fits():
            self.game_over = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside_boundary() or not self.block_fits():
            self.current_block.undo_rotation()
            return
        self.rotate_sound.play()

    def block_inside_boundary(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside_boundary(tile.row, tile.column):
                return False
        return True

    def reset(self):
        self.game_over = False
        self.grid.reset()
        self.blocks = [
            LBlock(),
            JBlock(),
            IBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def draw(self, screen: pygame.Surface):
        self.grid.draw(screen)
        self.current_block.draw(screen)

        match self.next_block.id:
            case 3:  # IBlock
                self.next_block.draw(screen, 255, 280)
            case 4:  # OBlock
                self.next_block.draw(screen, 255, 290)
            case _:
                self.next_block.draw(screen, 270, 270)
