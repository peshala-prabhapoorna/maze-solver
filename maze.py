import random
import time

from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self._num_cols):
            col = []
            for _ in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.015)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        col_index = self._num_cols - 1
        row_index = self._num_rows - 1
        self._cells[col_index][row_index].has_bottom_wall = False
        self._draw_cell(col_index, row_index)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_cells = []

            # check if adjacent cells exist and are visited
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_cells.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_cells.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_cells.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_cells.append((i, j + 1))

            # if there are no cells to move to
            if len(next_cells) == 0:
                self._draw_cell(i, j)
                return

            # randomly pick the next cell
            direction = random.randrange(len(next_cells))
            (next_i, next_j) = next_cells[direction]

            # break down walls
            # left
            if next_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            # right
            if next_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            # up
            if next_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            # down
            if next_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            # move to the chosen cell
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
