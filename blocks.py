from enum import Enum

import pygame

from colors import Colors
from position import Position


class RotationState(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def next(self) -> "RotationState":
        val = (self.value + 1) % 4
        return RotationState(val)

    def previous(self) -> "RotationState":
        val = abs((self.value - 1) % 4)
        return RotationState(val)


class Block:
    id: int
    cells: dict[RotationState, tuple[Position]]
    row_offset: int
    column_offset: int
    rotation_state: RotationState
    colors: tuple[Colors]

    def __init__(self, id: int):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = RotationState.UP
        self.colors = Colors.get_cell_colors()

    def move(self, rows: int, columns: int):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self) -> list[Position]:
        tiles = self.cells[self.rotation_state]
        move_tiles: list[Position] = []

        for position in tiles:
            position = Position(
                position.row + self.row_offset,
                position.column + self.column_offset,
            )
            move_tiles.append(position)

        return move_tiles

    def rotate(self):
        self.rotation_state = self.rotation_state.next()

    def undo_rotation(self):
        self.rotation_state = self.rotation_state.previous()

    def draw(self, screen: pygame.Surface, offset_x: int = 11, offset_y: int = 11):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)


class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            RotationState.UP: (
                Position(0, 2),
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
            ),
            RotationState.RIGHT: (
                Position(0, 1),
                Position(1, 1),
                Position(2, 1),
                Position(2, 2),
            ),
            RotationState.DOWN: (
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
                Position(2, 0),
            ),
            RotationState.LEFT: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 1),
                Position(2, 1),
            ),
        }
        self.move(0, 3)


class JBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            RotationState.UP: (
                Position(0, 0),
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
            ),
            RotationState.RIGHT: (
                Position(0, 1),
                Position(0, 2),
                Position(1, 1),
                Position(2, 1),
            ),
            RotationState.DOWN: (
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
                Position(2, 2),
            ),
            RotationState.LEFT: (
                Position(0, 1),
                Position(1, 1),
                Position(2, 0),
                Position(2, 1),
            ),
        }
        self.move(0, 3)


class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            RotationState.UP: (
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
                Position(1, 3),
            ),
            RotationState.RIGHT: (
                Position(0, 2),
                Position(1, 2),
                Position(2, 2),
                Position(3, 2),
            ),
            RotationState.DOWN: (
                Position(2, 0),
                Position(2, 1),
                Position(2, 2),
                Position(2, 3),
            ),
            RotationState.LEFT: (
                Position(0, 1),
                Position(1, 1),
                Position(2, 1),
                Position(3, 1),
            ),
        }
        self.move(-1, 3)


class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            RotationState.UP: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
            ),
            RotationState.RIGHT: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
            ),
            RotationState.DOWN: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
            ),
            RotationState.LEFT: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
            ),
        }
        self.move(0, 4)


class SBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            RotationState.UP: (
                Position(0, 1),
                Position(0, 2),
                Position(1, 0),
                Position(1, 1),
            ),
            RotationState.RIGHT: (
                Position(0, 1),
                Position(1, 1),
                Position(1, 2),
                Position(2, 2),
            ),
            RotationState.DOWN: (
                Position(1, 1),
                Position(1, 2),
                Position(2, 0),
                Position(2, 1),
            ),
            RotationState.LEFT: (
                Position(0, 0),
                Position(1, 0),
                Position(1, 1),
                Position(2, 1),
            ),
        }
        self.move(0, 3)


class TBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            RotationState.UP: (
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
            ),
            RotationState.RIGHT: (
                Position(0, 1),
                Position(1, 1),
                Position(1, 2),
                Position(2, 1),
            ),
            RotationState.DOWN: (
                Position(1, 0),
                Position(1, 1),
                Position(1, 2),
                Position(2, 1),
            ),
            RotationState.LEFT: (
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
                Position(2, 1),
            ),
        }
        self.move(0, 3)


class ZBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            RotationState.UP: (
                Position(0, 0),
                Position(0, 1),
                Position(1, 1),
                Position(1, 2),
            ),
            RotationState.RIGHT: (
                Position(0, 2),
                Position(1, 1),
                Position(1, 2),
                Position(2, 1),
            ),
            RotationState.DOWN: (
                Position(1, 0),
                Position(1, 1),
                Position(2, 1),
                Position(2, 2),
            ),
            RotationState.LEFT: (
                Position(0, 1),
                Position(1, 0),
                Position(1, 1),
                Position(2, 0),
            ),
        }
        self.move(0, 3)
