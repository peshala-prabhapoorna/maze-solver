import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 28
        num_rows = 20
        m1 = Maze(50, 50, num_rows, num_cols, 25, 25)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)

        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False
        )

    def test_maze_reset_visited_cells(self):
        num_cols = 28
        num_rows = 20
        m1 = Maze(50, 50, num_rows, num_cols, 25, 25, seed=70)

        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertEqual(m1._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
