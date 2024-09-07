from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    Maze(50, 50, 10, 14, 50, 50, win, 81)

    win.wait_for_close()


main()
