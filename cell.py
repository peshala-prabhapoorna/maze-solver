from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        p1 = Point(x1, y1)
        p2 = Point(x1, y2)
        fill_color = "white"
        if self.has_left_wall:
            fill_color = "black"
        self._win.draw_line(Line(p1, p2), fill_color)

        p1 = Point(x2, y1)
        p2 = Point(x2, y2)
        fill_color = "white"
        if self.has_right_wall:
            fill_color = "black"
        self._win.draw_line(Line(p1, p2), fill_color)

        p1 = Point(x1, y1)
        p2 = Point(x2, y1)
        fill_color = "white"
        if self.has_top_wall:
            fill_color = "black"
        self._win.draw_line(Line(p1, p2), fill_color)

        p1 = Point(x1, y2)
        p2 = Point(x2, y2)
        fill_color = "white"
        if self.has_bottom_wall:
            fill_color = "black"
        self._win.draw_line(Line(p1, p2), fill_color)

    def draw_move(self, to_cell, undo=False):
        x = (self._x1 + self._x2) // 2
        y = (self._y1 + self._y2) // 2
        p1 = Point(x, y)
        x = (to_cell._x1 + to_cell._x2) // 2
        y = (to_cell._y1 + to_cell._y2) // 2
        p2 = Point(x, y)
        line = Line(p1, p2)

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self._win.draw_line(line, fill_color)
