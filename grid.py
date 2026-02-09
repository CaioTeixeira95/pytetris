import pygame

from colors import Colors


class Grid:
    rows: int
    cols: int
    cell_size: int
    grid: list[list[int]]

    def __init__(self) -> None:
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self) -> None:
        for row in range(self.rows):
            for column in range(self.cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside_boundary(self, row: int, column: int) -> bool:
        return (0 <= row < self.rows) and (0 <= column < self.cols)

    def is_empty(self, row: int, column: int) -> bool:
        return self.grid[row][column] == 0

    def is_row_full(self, row: int):
        for column in range(self.cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row: int):
        for column in range(self.cols):
            self.grid[row][column] = 0

    def move_row_down(self, row: int, num_rows: int):
        target_row = row + num_rows
        for column in range(self.cols):
            self.grid[target_row][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self) -> int:
        completed_rows = 0
        for row in range(self.rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed_rows += 1
            elif completed_rows > 0:
                self.move_row_down(row, completed_rows)
        return completed_rows

    def reset(self):
        for row in range(self.rows):
            for column in range(self.cols):
                self.grid[row][column] = 0

    def draw(self, screen: pygame.Surface) -> None:
        for row in range(self.rows):
            for column in range(self.cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 11,
                    row * self.cell_size + 11,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
